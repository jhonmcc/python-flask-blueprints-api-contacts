import sys, os; sys.path.insert(0,os.path.dirname(os.path.dirname(__file__)))
from flask import Blueprint
from flask import Response, request
import json

sys.stdout.flush()
# objeto auxiliar para definir as rotas
user_routes = Blueprint('user_routes', __name__)

# definindo rotas para a blueprint
@user_routes.route('/', methods=['GET'])
def index_user():
    print('path user index acionada', flush=True)
    return json.dumps({"route": "user index"}, separators=(",", ":")).encode("utf-8")
