
"""
for login
"""

from ..routes import route
import base

@route(r'/login')
class LoginHandler(base.BaseHandler):
    def get(self):
        appid = self.get_argument('appid')
