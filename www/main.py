import logging
from aiohttp import web
import asyncio

from orm import get_mysql_pool
from routes import setup_routes

logging.basicConfig(level=logging.INFO)

loop = asyncio.get_event_loop()
mysql = loop.run_until_complete(get_mysql_pool(loop))
app = web.Application(loop=loop, debug=True)
app['mysql'] = mysql
setup_routes(app)
web.run_app(app)
