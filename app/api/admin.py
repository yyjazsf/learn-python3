from flask import Blueprint
from flask_restful import Resource, Api

from .. import app
admin = Blueprint('admin', __name__, url_prefix='/admin')
api = Api(admin)


class Home(Resource):
    def get(self):
        return 'admin home'

    def post(self):
        return {'methon': 'admin post'}


api.add_resource(Home, '/')


app.register_blueprint(admin)
