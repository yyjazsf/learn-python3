import logging
from datetime import datetime
import asyncio
from flask import Flask, session, redirect, url_for, escape, request, jsonify

from flask_sqlalchemy import SQLAlchemy

from .config import config

conf = config.get_config()

logging.basicConfig(level=logging.WARN)

app = Flask(__name__)


# can't use conf.database
app.config['SQLALCHEMY_DATABASE_URI'] = conf['database']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# init router
from . import api
from .api import admin
