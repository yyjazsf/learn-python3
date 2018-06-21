import logging
from datetime import datetime
from flask import Flask, session, redirect, url_for, escape, request, jsonify
from flask_httpauth import HTTPTokenAuth
from flask_sqlalchemy import SQLAlchemy

from . import config

conf = config.get_config()

logging.basicConfig(level=logging.WARN)

app = Flask(__name__)
auth = HTTPTokenAuth()

from .api import api_blueprint, admin_blueprint

# can't use conf.database
app.config['SQLALCHEMY_DATABASE_URI'] = conf['database']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# init router
app.register_blueprint(api_blueprint)
app.register_blueprint(admin_blueprint)
