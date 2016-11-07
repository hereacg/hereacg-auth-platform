
"""
Configs for website
"""

from os import path


app_configs={
'debug': True,
'static_path': path.join('.','static')
}

database_configs={
'mongo_uri': 'mongo://localhost/auth' 
}

