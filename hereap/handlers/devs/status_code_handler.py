

from ..base import BaseHandler

class Return200Handler(BaseHandler):
    def get(self):
        self.logger.debug('Return200Handler Visited.')
        self.set_status(200)
