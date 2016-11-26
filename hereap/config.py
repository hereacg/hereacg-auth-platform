
"""
Configs for website
"""

from os import path


app_configs={
'debug': True,
'static_path': path.join('.','static')
}

database_configs={
'mongo_uri': os.getenv('OPENSHIFT_MONGODB_URL') or 'mongo://localhost/auth'
}
