
"""
Routes for website
"""
from config import app_configs as _app_c
from handlers.devs.status_code_handler import Return200Handler

routes=[]


_dev_routes=[(r'/dev/r200',Return200Handler)]


if _app_c['debug']:
    routes[len(routes):] = _dev_routes[:]
