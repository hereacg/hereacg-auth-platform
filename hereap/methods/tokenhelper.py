

"""
helper function for token
"""

from . import db
from ..util import ranstr

_client = db.client()['tokens']


def new_token(*args,**kargs):
    """
    (*args,**kargs) -> (*str,**(str=(str,int,list)) -> str

    Get a new token.
    """
    _randomstr = ranstr(*args)
    _doc = {
    'token': _randomstr
    }
    _doc.update(kargs)
    _client.insert(_doc)
    return _randomstr


def find_token(token):
    """
    (token) -> (str) -> dict

    Get doc from token
    Note: dict not built-in dict
    """
    return _client.find_one({
    'token':token
    })


def remove_token(token):
    """
    (token) -> (str) -x

    Remove a token
    """
    find_token(token).remove()
