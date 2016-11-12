

"""
Base test
"""

import unittest
from ..methods import db

class TestCase(unittest.TestCase):
    def setUp(self):
        """
        Ready test
        """
        self._db = db.client()
        for f in self._s_f:
            f(self)

    def prepare(self,func):
        if not self._s_f:
            self._s_f = []
        self._s_f.append()

    def tearDown(self):
        """
        Stop test
        """
        for db in self._db:
            db.find({
            'istest':True
            }).remove()
        for f in self._fi_f:
            f(self)

    def finishall(self,func):
        if not self._fi_f:
            self._fi_f = []
        self._fi_f.append(func)
