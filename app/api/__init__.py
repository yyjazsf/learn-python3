from flask import Blueprint
from flask_restful import Resource, Api

from .. import app, login_manager

api_root = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_root)  # errors or catch_all_404s=True

login_manager.init_app(api_root)

# public


class Index(Resource):
    def get(self):

        return {}


api.add_resource(Index, '/', '/index')


class Login(Resource):
    def post(self):
        return {}


api.add_resource(Login, '/login')


class SignUp(Resource):
    def post(self):
        return {}


api.add_resource(SignUp, '/signup')


# need auth
class User(Resource):
    def get(self):
        return {'url': 'get /user'}


api.add_resource(User, '/user')


app.register_blueprint(api_root)
