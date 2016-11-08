
"""
Permission helper function
"""

from .db import client
from ..util import ranstr


_per = []


_client = client()['permission']


def _get_new_per_id():
    """
    () -> str
    
    Return a new perid.
    """
    length = _client.count()
    s = ranstr(str(length))
    return s


def _new_doc(perid,**kargs):
    """
    (perid,**kargs) -> (str,**object) -> cur
    
    Get a new doc.
    """
    _client.insert(dict(id=perid,**kargs))
    return _client.find_one(dict(id=perid))


class Permission(object):
    def __init__(self):
        pass
    
    @classmethod
    def new(self,**kargs):
        """
        (**kargs) -> (**object) -> cur
        
        Add a new doc for a new perid, return perid.
        """
        c = _new_doc(_get_new_per_id(),**kargs)
        for v in _per:
            c.update({
                '$set': {
                    v['name']: v['default']
                }
            })
        return c['id']
    
    @classmethod
    def add(self,name,default=None):
        """
        (name,default=None) -> (str,object) -x
        Add a new permission item.
        """
        _per.append(
        dict(name=name,default=default)
        )
        return self
    
    @classmethod
    def _set(self,obj,name,value):
        """
        (obj,name,value) -> (object,str,object) -x
        
        Set a object's permission item.
        """
        obj.update({
            '$set':{
                name:value
            }
        })
    
    @classmethod
    def set(self,role={},perid=None,name,value):
        """
        (role={},perid=None,name,value) -> (dict,str,str,object) -> self
        
        Set a doc's permission item.
        """
        find_role = dict(**role)
        if perid: find_role.extend({'id':perid})
        c = _client.find_one(find_role)
        self._set(c,name,value)
        return self
    
    @classmethod
    def get_set(self,role={},perid=None):
        """
        (role={},perid=None) -> (dict,str) -> cur
        
        Return the set for doc.
        """
        find_role = dict(**role)
        if perid: find_role.extend({'id':perid})
        return _client.find_one(find_role)
    
    @classmethod
    def get(self,role={},perid=None,name):
        """
        (role={},perid=None,name) -> (dict,str,str) -> object
        
        Return singal value of set.
        """
        return self.get_set(role=role,perid=perid)[name]
    
    
        
        