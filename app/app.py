import logging
import os
import json
import time
import asyncio
from datetime import datetime

import yaml
from aiohttp import web

logging.basicConfig(level=logging.WARN)


def index(req):
    return web.Response(body='<h1>blog</h1>')


app = web.Application()

# app.add_routes()
web.run_app(app)
