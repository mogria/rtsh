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
    return {prop: getattr(obj, prop) for prop in included_properties}

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

    def __init__(self, obj):
        if isinstance(obj, GameObject):
            self._obj = obj
            self._old_storage_location = obj.storage_location()
            self._old_symlinks = obj.symlinks()
        else:
            raise ValueError("can only store GameObject's")

    @staticmethod
    def from_file(filename):
        obj = Storage._read(filename)
        return Storage(obj)

    def __enter__(self):
       self.read()
       return self._obj

    def __exit__(self, type, value, traceback):
       self.write()

    def read(self):
        self._obj = Storage._read(self._old_storage_location)
        return self._obj

    @staticmethod
    def _read(filename):
        result = {}
        with open(filename, "r") as f:
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

    def write(self):
        # make sure the current storage location is still up to date
        new_location = Storage._remove_if_old(self._old_storage_location, self._obj.storage_location())
        self._old_storage_location = self._obj.storage_location()
        
        new_symlinks = self._obj.symlinks()
        if new_location:
            # if the storage location changed all the symlinks need to be recreated
            # so just delete them in here
            for symlink in self._old_symlinks:
                os.remove(symlink)
        else:
            # this is based on the assumtion that the same game object
            # always returns the same amount of symlinks
            for idx, old_link in enumerate(self._old_symlinks):
                res = Storage._remove_if_old(old_link, new_symlinks[idx])
        self._old_symlinks = new_symlinks

        # make sure the directory for the file exists
        Storage._make_required_dirs(self._old_storage_location)

        # write the file (possibly to a new location)
        with open(self._old_storage_location, "w") as f:
            json_properties = filterproperties(self._obj)
            json_properties["class"] = json_properties["classname"]
            del json_properties["classname"]
            json.dump(json_properties, f, indent=4, sort_keys=True)
            f.write('\n') # add addtional \n for better viewing on shell

        # create new symlinks
        for new_link in self._old_symlinks:
            if not os.path.lexists(new_link):
                Storage._make_required_dirs(new_link)
                os.symlink(self._old_storage_location, new_link)

    @staticmethod
    def _remove_if_old(old_location, new_location):
        """removes old files when the storage location or the symlink location changed"""
        if new_location != old_location:
            if os.path.lexists(old_location):
                os.unlink(old_location)
            return True
        return False

    @staticmethod
    def _make_required_dirs(new_file_to_be_written):
        directory = os.path.dirname(new_file_to_be_written)
        if not os.path.exists(directory):
            os.makedirs(directory)
