import inspect

def getproperties(obj):
    """returns all the @property annotated properties of an object"""
    return [k for k,v in inspect.getmembers(obj.__class__, lambda x: isinstance(x, property))]

def filterobject(obj, included_properties):
    """only return certain properties of an object"""
    return {prop: getattr(obj, prop) for prop in included_properties}

def filterproperties(obj):
    """get a dictionary of an object with only @property annotated properties"""
    return filterobject(obj, getproperties(obj))

