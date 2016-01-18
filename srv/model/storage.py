import json
import inspect
from tile import Tile
from gameobject import GameObject

class InvalidGameObectError(Exception):
    def __init__(self, file, message, inner_exception = None):
        self.file = file
        self.message = message
        self.inner_exception = inner_exception

def getproperties(obj):
    """returns all the @property annotated properties of an object """
    return [k for k,v in inspect.getmembers(obj.__class__, lambda x: isinstance(x, property))]

def filterdict(dict, included_keys):
    """only return certain keys of a dictionary"""
    return {k: dict[k] for k in dict if k in included_keys}

def filterobject(obj, included_properties):
    """only return certain properties of an object"""
    return filterdict(obj.__dict__, included_properties)

def filterproperties(obj):
    """get a dictionary of an object with only @property annotated properies"""
    return filterobject(obj, getproperties(obj))

class Storage(object):
    game_object_classes = {
        'unit': None,
        'building': None,
        'tile': Tile,
        'world': None,
    }

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        result = {}
        with open(self.filename, "r") as f:
            try:
                result = json.load(f) 
            except ValueError as e:
                raise InvalidGameObjectError(f, "couldn't parse game object file", e)
        if not "classname" in result:
            raise InvalidGameObjectError(f, "no 'class' indicator found, can't handle this game object")

        result["classname"] = result["class"]
        del result["class"]

        if not result["class"] in game_object_classes:
            raise InvalidGameObjectError(f, "invalid 'class' indicator '" + result["class"] + "'. No known classtype.")

        return game_object_classes[result["class"]](**result)

    def write(self, obj):
        if not isinstance(obj, GameObject):
            raise ValueError("only GameObject and it's subtypes can be written by GameObjectPersistence")

        with open(self.filename, "w") as f:
            json_properties = filterproperties(obj)
            json_properties["class"] = json_properties["classname"]
            del json_properties["classname"]
            json.dump(json_properties, f, indent=True)

