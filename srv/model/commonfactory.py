
class ConstructionError(Exception):
    def __init__(self, object_name, object_type, message):
        super(ConstructionError, self).__init__("Construction error with {0}_type '{1}': {2}".format(object_name, object_type, message))

def CommonFactory(object_name, object_type, object_types, *args, **kwargs):
    """common factory for buildings and units (as of now)
        object_name - the name of the object which should be passed onto the error messages 
        object_type - the type of the object which should be constructed, needs to be a key in object_types
        object_types - a dictionary with all the object_type's as key and a callable function/classname as value"""
    if not is_valid_object_type(object_type, object_types):
        raise ConstructionError(object_name, object_type, "no such {0} type".format(object_name))
    object_class = object_types[object_type]
    if object_class is None:
        raise ConstructionError(object_name, object_type, "{0} not yet implemented".format(object_name))
    obj = object_class(*args, **kwargs)
    obj.dirty()
    return obj

def is_valid_object_type(object_type, object_types):
    return object_type in object_types;

