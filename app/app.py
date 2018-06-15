#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import time
import logging
from datetime import datetime
import asyncio
from flask import Flask, session, redirect, url_for, escape, request, jsonify

from config import config
import db

logging.basicConfig(level=logging.WARN)
print(config.get_config())


db.create_pool()
# db.execute('INSERT INTO `blog`.`user` (`username`,`password`) VALUES (?,?);',
#            ('admin', 'admin'))
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    data = db.query('select * from user')
    return jsonify(data)
