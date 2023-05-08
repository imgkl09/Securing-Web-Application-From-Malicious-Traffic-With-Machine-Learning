from flask import Request
import joblib
from skfuzzy import control as ctrl
from env.ml_config import PAYLOAD_FILE_PATH, PAYLOAD_ML_MODELS
from env.proxy_config import ROASTING_ML_MODELS 
from WAF_Model_Trainer.utils import extract_feature

file_path = PAYLOAD_FILE_PATH + "/" + PAYLOAD_ML_MODELS[ROASTING_ML_MODELS["payloads"]]
#print(file_path)

def block_malicious_payloads(request : Request):
    try:
        with open(file_path , "rb") as f:
            model = joblib.load(f)
       
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

        if not args_str:
            return 0
        
        args_str.rsplit(' ',1)[0]
        print("\n\nPayload Data --> " + args_str )
        d = extract_feature(args_str)
        result = model.predict(d.drop(["payloads"],axis=1).values)
        return result[0]

    except Exception as e:
        print(e)
        return 0
