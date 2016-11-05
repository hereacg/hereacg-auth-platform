
"""
some help function
"""

import config as _c
from hashlib import sha512
from routes import routes
from tornado.web import Application
from time import time as get_time_sec


def get_application():
    """
    () -> tornado.web.Application

    Get a application from configs.
    """
    return Application(handlers=routes,**_c.app_configs)


def simple_hash(func,sdata):
    """
    (func,sdata) -> (function,str) -> str

    More easy for hashlib
    """
    return func(bytes(sdata,'utf8')).hexdigest()


def ranstr(*args):
    """
    (*args) -> (*str) -> str

    Get a random string.
    """
    return simple_hash(sha512,bytes(''.join(str(get_time_sec()),*args)))
