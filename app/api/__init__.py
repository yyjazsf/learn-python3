from flask import Blueprint
from flask_restful import Resource, Api

from .. import app
api_root = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_root)


class Home(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {'methon': 'post'}


api.add_resource(Home, '/')


class User(Resource):
    def get(self):
        return {'url': 'get /user'}


api.add_resource(User, '/user')


app.register_blueprint(api_root)
