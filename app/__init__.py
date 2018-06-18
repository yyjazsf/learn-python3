import logging
from datetime import datetime
import asyncio
from flask import Flask, session, redirect, url_for, escape, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

from .config import config

conf = config.get_config()

logging.basicConfig(level=logging.WARN)

app = Flask(__name__)
api = Api(app)

# can't use conf.database
app.config['SQLALCHEMY_DATABASE_URI'] = conf['database']
db = SQLAlchemy(app)

# init router
from . import resources
