from flask import Flask
from env.server_config import *
from WAF.Request_Handlers.router import request_handlers

app = Flask(__name__)

def create_server(config_file : str ='env.server_config.ProductionConfig') -> None:

    app.config.from_object(config_file)
    app.register_blueprint(request_handlers)
    print(f"Server started at { app.config['HOST']} port : {app.config['PORT']}")
    app.run(host=app.config["HOST"] , port=app.config["PORT"])

