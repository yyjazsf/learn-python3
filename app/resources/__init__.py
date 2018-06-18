
from app import api
from flask_restful import Resource


class Home(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(Home, '/')


class User(Resource):
    def get(self):
        return {'url': 'get /user'}


api.add_resource(User, '/user')
