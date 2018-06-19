from flask import Blueprint
from flask_restful import Resource, Api

from .. import app
api_root = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_root)


class Login(Resource):
    def post(self):
        return {'methon': 'post'}


api.add_resource(Login, '/login')


class User(Resource):
    def get(self):
        return {'url': 'get /user'}


api.add_resource(User, '/users')


app.register_blueprint(api_root)
