from flask import Blueprint
from flask_restful import Resource, Api

admin_blueprint = Blueprint('admin', __name__, url_prefix='/admin')
api = Api(admin_blueprint)


class Home(Resource):
    def get(self):
        return 'admin home'

    def post(self):
        return {'methon': 'admin post'}


api.add_resource(Home, '/')
