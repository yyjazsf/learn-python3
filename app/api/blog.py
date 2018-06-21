from flask import Blueprint, jsonify, g
from flask_restful import Resource, Api

from app import auth

api_blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_blueprint)  # errors or catch_all_404s=True


@auth.verify_token
def verify_token(token):
    # client http header Authorization
    # todo verify_token from redis
    return True


@auth.error_handler
def unauth():
    return jsonify({
        'code': 401,
    })


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
    @auth.login_required
    def get(self):
        return {'url': 'get /user'}


api.add_resource(User, '/user')
