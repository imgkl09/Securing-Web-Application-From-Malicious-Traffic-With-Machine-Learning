from flask import Blueprint ,request , Response , make_response , render_template
from WAF.WAF_Layers.bad_useragents import block_baduseragents
from WAF.WAF_Layers.malicious_payloads import block_malicious_payloads
from WAF.Request_Handlers.utils import get_payload
import csv
from datetime import date,datetime
from env.http_config import HTTP_CONFIG
from WAF.Request_Handlers.controller import *
from env.proxy_config import BACKENDSERVER
#from WAF.load_balancer.balancer_algo import BalancerAlgo
from Threat_Identification.attack_identifier import identify_attack

request_handlers = Blueprint('request_handlers',__name__,url_prefix="")

@request_handlers.route("/<path:path>" , methods=HTTP_CONFIG["allowed_methods"])
@request_handlers.route("/",methods=HTTP_CONFIG["allowed_methods"])
def request_handler(path : str ="") -> Response:
    
    real_url = BACKENDSERVER[0]+f"/{path}"
    #real_url =f"{server_name}/{path}"
    if HTTP_CONFIG["block_bad_useragents"] :
        is_bad_ua = block_baduseragents(request)   
        print(request)
        if is_bad_ua:
            
            print(f"\nBad User Agent!!! |URL : {real_url} |  |METHOD : {request.method} |Ip : {request.remote_addr}|User-Agent : {request.headers['User-Agent']} ")            
            x = date.today()
            y = datetime.now()
            data = [request.headers['User-Agent'], real_url , x , y.strftime("%H:%M:%S") ]


            with open('Logged_Output/waf_user_agents.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data)
            return make_response(render_template("blocked.html")
                            ,HTTP_CONFIG["blocked_status_code"]
                            ,HTTP_CONFIG["blocked_response_headers"])
    
    if HTTP_CONFIG["block_malicious_payloads"] :
        is_malicious_req = block_malicious_payloads(request)

        if is_malicious_req:
            
            print(f"\nMalicious Payload!!! |URL : {real_url} |  |METHOD : {request.method} |Ip : {request.remote_addr} ")
            x = date.today()
            y = datetime.now()
            data = [get_payload(request), real_url , x , y.strftime("%H:%M:%S") ]


            with open('Logged_Output/waf_payloads.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data)
            
            paydata=[get_payload(request),identify_attack(get_payload(request))]
            with open('Logged_Output/bnns_attack_types.csv', 'a',encoding='UTF8', newline='') as g:
                writer=csv.writer(g)
                writer.writerow(paydata)
            return make_response(render_template("blocked.html")
                                    ,HTTP_CONFIG["blocked_status_code"]
                                    ,HTTP_CONFIG["blocked_response_headers"])
    


    
    print(f"\nURL : {real_url} |  |METHOD : {request.method} |Ip : {request.remote_addr}")


    # routing to particular http method controller
    if request.method == "GET":
        return get_handler(real_url)

    elif request.method == "POST":
        return post_handler(real_url)
    elif request.method == "PUT":

        return put_handler(real_url)

    elif request.method == "DELETE":

        return delete_handler(real_url)
    
    else : 
        return default_handler(real_url)