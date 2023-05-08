from flask import Request
import joblib
from env.ml_config import UA_FILE_PATH, UA_ML_MODELS
from env.proxy_config import ROASTING_ML_MODELS 

file_path = UA_FILE_PATH + "/" + UA_ML_MODELS[ROASTING_ML_MODELS["user-agents"]]
#print(file_path)




def block_baduseragents(request : Request):
    try:
        with open(file_path , "rb") as f:
            model = joblib.load(f)
        result = model.predict([request.headers["User-Agent"]])
        print("\n\nUser Agent -->  " + request.headers["User-Agent"] )        
        return result[0]

    except Exception as e:
        print(e)
        return 0

