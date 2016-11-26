

"""
Test for tokenhelper
"""

from basetest import TestCase
from ..methods import tokenhelper as token


class TokenHelperTest(TestCase):
    def test_can_create_token_and_save_to_database(self):
        _t_str = token.new_token(
        'ToeknTest',
        'istest'=True
        )
        _st = self._db['tokens'].find_one({
        'token':_t_str
        'istest':True
        })
        
