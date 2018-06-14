import logging
import os
import json
import time
import asyncio
from datetime import datetime
from aiohttp import web

logging.basicConfig(level=logging.WARN)


def index(req):
    return web.Response(body='<h1>blog</h1>')


async def init(loop):
    app = web.Application(loop=loop)
