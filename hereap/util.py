
"""
some help function
"""

import config
from routes import routes
from tornado.web import Application


def get_application():
    return Application(handlers=routes,**config.app_configs)
