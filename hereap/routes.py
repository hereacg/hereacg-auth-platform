
"""
Routes for website
"""
from config import app_configs as _app_c

routes=[]

from handlers.devs.status_code_handler import Return200Handler

_dev_routes=[(r'/dev/r200',Return200Handler)]


def route(c,url,**kargs):
    if len(kargs) > 0:
        routes.append((url,c))
    else:
        routes.append((url,c,kargs))
    def route_d(c,*args,**kargs):
        return c
    return route_d

from handlers.login import LoginHandler



if _app_c['debug']:
    routes[len(routes):] = _dev_routes[:]