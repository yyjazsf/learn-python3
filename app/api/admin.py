from flask import Blueprint, jsonify
from flask_restful import Resource, Api

import json

from app import db
from app import auth
from .. import models
from ..utils import success, error

admin_blueprint = Blueprint('admin', __name__, url_prefix='/api/admin')
api = Api(admin_blueprint)


@auth.verify_token
def verify_token(token):
    # client http header Authorization
    # todo verify_token from redis
    return True


@auth.error_handler
def unauth():
    return error(status=401, message='无权限')


class Home(Resource):
    def get(self):
        return 'admin home'


api.add_resource(Home, '/')


class User(Resource):
    @auth.login_required
    def get(self):
        res = models.User.query.limit(2).all()

        return success(data={
            "list": list(models.UserSchema(many=True).dump(res).data)
        })


api.add_resource(User, '/user')


'''
system util
'''


class Init(Resource):
    def get(self):
        db.create_all()


api.add_resource(Init, '/init')


class Reset(Resource):
    def get(self):
        db.drop_all()


api.add_resource(Reset, '/reset')
