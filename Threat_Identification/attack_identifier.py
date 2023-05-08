from WAF_Model_Trainer.utils import extract_feature
import numpy as np
import torch,joblib,pickle
from env.ml_config import ATTACK_IDENTIFICATION_FILE_PATH,ATTACK_IDENTIFICATION_MODELS
from env.proxy_config import ROASTING_ML_MODELS

       
import joblib
import sys
sys.path.append('C:/Users/gokul/Desktop/Attack_Identification/Threat_Identification') # Add the path of the module containing the BayesianNN class to the sys.path
from Bayesian_Network import BayesianNN # Import the BayesianNN class from the module

def predict(model, data):
    model.eval()
    with torch.no_grad():
        outputs = model(data)
        _, predicted = torch.max(outputs.data, 1)
    return predicted

def identify_attack(current_payload):
    
    try:
        # Load the saved pipeline object
        model = joblib.load('C:/Users/gokul/Desktop/Attack_Identification/Threat_Identification/bnn.pkl')     
        d = extract_feature(current_payload)
        d.drop(columns=d.columns[0], axis=1,  inplace=True)
        im_arr = np.array(d.values)
        im_arr = im_arr.flatten()
        current_data = torch.Tensor(im_arr)
        predicted_class = predict(model, current_data.unsqueeze(0))
        if(predicted_class.item() == 0) :
            attack_type = "NORMAL"
        elif(predicted_class.item() == 1) :
            attack_type = "COMMAND INJECTION"
        elif(predicted_class.item() == 2) :
            attack_type = "SQL INJECTION"
        else:
            attack_type = "CROSS-SITE SCRIPTING (XSS)"
        
        return attack_type
    
    except Exception as e:
        print(e)
        return -1
