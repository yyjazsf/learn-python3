import logging

from flask import Flask
from flask_httpauth import HTTPTokenAuth
from flask_sqlalchemy import SQLAlchemy

from . import config

conf = config.get_config()

logging.basicConfig(level=logging.WARN)

app = Flask(__name__)
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
