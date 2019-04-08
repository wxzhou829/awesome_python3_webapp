__author__ = 'Zhou Wei'
import logging
from aiohttp import web


async def index(request):
    return    web.Response(body='<h1>Awesome</h1>'.encode('utf-8'),
                content_type='text/html')


async def squ(request):
    async with request.app['mysql'].acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT 42;")
            print(cur.description)
            (r,) = await cur.fetchone()
            assert r == 42
            await cur.execute('select * from pet;')
            lines = await cur.fetchall()
            for line in lines:
                print(line)

    return web.Response(text='Hello Aiohttp!')

