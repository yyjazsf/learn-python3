import logging

from flask import Flask
from flask.json import JSONEncoder
from flask_httpauth import HTTPTokenAuth
from flask_sqlalchemy import SQLAlchemy

from . import config

conf = config.get_config()

logging.basicConfig(level=logging.WARN)


# class CustomJSONEncoder(JSONEncoder):
#     def default(self, obj):
#         try:
#             print('=============', isinstance(obj, db.Model))
#             if isinstance(obj, db.Model):
#                 exclude_prefixes = (
#                     '__', '_{}__'.format(obj.__class__.__name__))
#                 return iter([[
#                     (k, v) for k, v in self.__class__.__dict__.iteritems()
#                     if not (k.startswith(exclude_prefixes) or hasattr(v, '__call__'))
#                 ]])
#             iterable = iter(obj)
#         except TypeError:
#             pass
#         else:
#             return list(iterable)
#         return JSONEncoder.default(self, obj)


app = Flask(__name__)
# app.json_encoder = CustomJSONEncoder

auth = HTTPTokenAuth()

# can't use conf.database
app.config['SQLALCHEMY_DATABASE_URI'] = conf['database']['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = conf['database']['SQLALCHEMY_TRACK_MODIFICATIONS']
app.config['SQLALCHEMY_POOL_RECYCLE'] = conf['database']['SQLALCHEMY_POOL_RECYCLE']
db = SQLAlchemy(app)

from . import models

from .api import api_blueprint, admin_blueprint

# init router
app.register_blueprint(api_blueprint)
app.register_blueprint(admin_blueprint)
