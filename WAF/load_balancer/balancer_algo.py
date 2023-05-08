from env.http_config import HTTP_CONFIG, LOAD_BALANCE_ALGO
from env.proxy_config import BACKENDSERVER


class BalancerAlgo:
    
    def __init__(self , algo_name : str = HTTP_CONFIG["load_balance_algo"]) -> None:
        
        self.algo_name = algo_name
        self.server_instance_count = len(BACKENDSERVER)
        self.current_instance = 0


    def balance(self) -> str:
        
        if self.algo_name == LOAD_BALANCE_ALGO["ROUND_ROBIN"]:
            #print("****Load balancing requests****")
            return self.round_robin()
        
        return BACKENDSERVER[0]

    def round_robin(self) -> str:
        
        ip = BACKENDSERVER[ (self.current_instance%self.server_instance_count) ]
        self.current_instance += 1
        return ip
