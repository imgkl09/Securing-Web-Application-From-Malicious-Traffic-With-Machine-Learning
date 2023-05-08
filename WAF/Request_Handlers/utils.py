from typing import List, Tuple
from env.http_config import HTTP_CONFIG
from flask import Request

def exclude_headers(response) -> List[Tuple[str,str]]:
    
    headers = [(key,response.headers[key]) for key in response.headers 
                                        if key.lower() not in HTTP_CONFIG["exclude_headers"]]

    return headers

def get_payload(request :  Request):
    args_str = ""
    if request.method == "GET":
        for _ , v  in request.args.items():
            args_str += v + " "

    else:
        if request.headers["Content-Type"].lower() == "application/json": 
            for _ , v in request.json.items():
                args_str += v + " "

        elif request.headers["Content-Type"].lower() == "multipart/form-data" or request.headers["Content-Type"].lower() == "application/x-www-form-urlencoded": 
            for _ , v in request.form.items():
                args_str += v + " "
        else:
            for _ , v  in request.args.items():
                args_str += v + " "

    args_str.rsplit(' ',1)[0]
    return args_str
