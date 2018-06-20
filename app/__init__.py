import logging
from datetime import datetime
from flask import Flask, session, redirect, url_for, escape, request, jsonify
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from .config import config

conf = config.get_config()

logging.basicConfig(level=conf['logging']['level'])

app = Flask(__name__)

login_manager = LoginManager()

# can't use conf.database
app.config['SQLALCHEMY_DATABASE_URI'] = conf['database']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# init router
from . import api
from .api import admin
