
"""
Base Handler
"""


from logging import getLogger
import methods.db as database
from .. import config as _c
import methods.tokenhelper as token
from tornado.web import RequestHandler

class BaseHandler(RequestHandler):
    @property
    def database(self):
        """
        () -> pymongo.MongoClient

        Return a mongodb database client from configs.
        """
        if not self._db:
            self._db = database.client()
        return self._db

    def get_current_user(self):
        """
        () -> dict

        Get current user, return a dict for from token
        """
        user_cookie = self.get_secure_cookie('user_token')
        if user_cookie:
            user=token.find_token(user_cookie)
            if user: return user
        return None

    @property
    def logger(self):
        """
        () -> logging.Logger

        Get logger
        """
        return getLogger(__name__)

    @property
    def _c(self):
        """
        () -> ..config

        Get configs.
        """
        return _c
