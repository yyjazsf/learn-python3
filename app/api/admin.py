from flask import Blueprint
from flask_restful import Resource, Api

from app import db

admin_blueprint = Blueprint('admin', __name__, url_prefix='/api/admin')
api = Api(admin_blueprint)


class Home(Resource):
    def get(self):
        return 'admin home'


api.add_resource(Home, '/')


class Init(Resource):
    def get(self):
        db.create_all()


api.add_resource(Init, '/init')
