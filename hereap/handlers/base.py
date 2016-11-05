
"""
Base Handler
"""

from logging import getLogger
import methods.db as database
from tornado.web import RequestHandler

class BaseHandler(RequestHandler):
    @property
    def database(self):
        return database.client()

    def get_current_user(self):
        user_cookie = self.get_secure_cookie('user')
        if user_cookie:
            return user_cookie
        return None

    @property
    def logger(self):
        return getLogger(__name__)
