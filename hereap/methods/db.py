
"""
function for db
"""

import config as _c
import pymongo

_db = None


def client():
    return pymongo.MongoClient(
    _c.database_configs['mongo_uri']
    )
