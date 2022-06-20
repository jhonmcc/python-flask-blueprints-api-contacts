import sys, os; sys.path.insert(0,os.path.dirname(os.path.dirname(__file__))) # esse comando vai te ajudar a fazer os import's de outras pastas

import json
import logging
# from flask_cors import CORS

from waitress import serve
from flask import Flask
from flask import request, Response

# imports de modulos blueprint criados
# from src.user.app import user_routes

# para dar um prefixo a api ele nao necessariamente é obrigatorio caso nao queira apenas remova a classe e comando de prefixo
# class PrefixMiddleware(object):
#     def __init__(self, app, prefix=''):
#         self.app = app
#         self.prefix = prefix

#     def __call__(self, environ, start_response):
#         if environ['PATH_INFO'].startswith(self.prefix):
#             environ['PATH_INFO'] = environ['PATH_INFO'][len(self.prefix):]
#             return self.app(environ, start_response)
#         else:
#             start_response('404', [('Content-Type', 'text/plain')])
#             return ['Essa url nao pode ser utizada acrescente o prefixo /api/'.encode()]

app = Flask(__name__)
# CORS(app)

# app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/api') # < seu prefixo aqui

# adicionar blueprints aqui
# app.register_blueprint(blueprint=user_routes, url_prefix='/user')

# rota basica
@app.route('/', methods=['GET'])
def initial_route():
    return 'api index route'
    # return json.dumps({"server": "online"}, separators=(",", ":")).encode("utf-8")


if __name__ == "__main__":
    try:
        port = int(os.environ.get('$PORT', 8080))
        serve(app, host='0.0.0.0', port=8080)
    except Exception as e:
        logging.error('Erro iniciando o servidor - ' + str(e))
        os._exit(0)
