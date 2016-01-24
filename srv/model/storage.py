import os
import json
import inspect
from model.tile import Tile
from model.world import World
from model.gameobject import GameObject
from model.unitfactory import UnitFactory
from model.buildingfactory import BuildingFactory
from model.resources import Resources

class InvalidGameObectError(Exception):
    def __init__(self, file, message, inner_exception = None):
        self.file = file
        self.message = message
        self.inner_exception = inner_exception

def getproperties(obj):
    """returns all the @property annotated properties of an object"""
    return [k for k,v in inspect.getmembers(obj.__class__, lambda x: isinstance(x, property))]

def filterobject(obj, included_properties):
    """only return certain properties of an object"""
    dictionary = dir(obj)
    return {k: getattr(obj, k) for k in dictionary if k in included_properties}

def filterproperties(obj):
    """get a dictionary of an object with only @property annotated properties"""
    return filterobject(obj, getproperties(obj))

class Storage(object):
    game_object_classes = {
        'unit': UnitFactory,
        'building': BuildingFactory,
        'tile': Tile,
        'world': World,
        'resources': Resources
    }

    def __init__(self, obj_or_filename):
        if isinstance(obj_or_filename, GameObject):
            self._filename = obj_or_filename.storage_location()
        else:
            self._filename = obj_or_filename

    def __enter__(self):
       self._obj = self.read()
       return self._obj

    def __exit__(self, type, value, traceback):
       self.write(self._obj)

    def read(self):
        result = {}
        with open(self._filename, "r") as f:
            try:
                result = json.load(f) 
            except ValueError as e:
                raise InvalidGameObjectError(f, "couldn't parse game object file", e)
        if not "class" in result:
            raise InvalidGameObjectError(f, "no 'class' indicator found, can't handle this game object")

        if not result["class"] in Storage.game_object_classes:
            raise InvalidGameObjectError(f, "invalid 'class' indicator '" + result["class"] + "'. No known classtype.")

        game_object_class = Storage.game_object_classes[result["class"]]
        del result["class"]
        return game_object_class(**result)

    def write(self, obj):
        if not isinstance(obj, GameObject):
            raise ValueError("only GameObject and it's subtypes can be written by GameObjectPersistence")

        # make sure the directory for the file exists
        directory = os.path.dirname(self._filename)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(self._filename, "w") as f:
            json_properties = filterproperties(obj)
            json_properties["class"] = json_properties["classname"]
            del json_properties["classname"]
            json.dump(json_properties, f, indent=4)

