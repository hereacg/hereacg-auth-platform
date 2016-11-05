

"""
Some helper function and class for user op.
"""

from . import db
from hashlib import sha512
from ..util import simple_hash
import tokenhelper as token

_client = db.client()['users']


class UserError(Exception):
    pass

class LoginError(UserError):
    pass


class User(object):
    def __init__(self,userid=None,username=None):
        """
        (userid=None,username=None) -> (int,str) -> self

        Create a user object by userid or username
        """
        self._user_id = _client.find_one({
        '$or': {
        'id':userid,
        'username':username
        }
        })['id']

    def login(self,pwd=None,hpwd=None):
        """
        (pwd=None,hpwd=None) -> (str,str) #-> (password,hashedpassword) -x

        Login a user by password
        """
        if not (pwd or hpwd): raise LoginError('Password is empty')
        tpass = hpwd or simple_hash(sha512,pwd)
        result = _client.find({
        'id': self._user_id,
        'password': tpass
        }).count()
        if not result > 0:
            raise LoginError('Wrong password')
        else:
            self._hashed_pass = tpass
            self.prepare_userinfo()
            self._token = token.new_token()

    def prepare_userinfo(self):
        """
        () -x

        Ready user info
        """
        result = _client.find_one({
        'id': self._user_id
        'password': self._hashed_pass
        },
        )
        del result['id']
        del result['password']
        for k in result:
            self.__dict__['_info_'+k] = result[k]

    
