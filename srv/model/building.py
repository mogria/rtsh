from model.gameobject import GameObject
from model.ownable import Ownable
from model.nameable import Nameable
from model.destroyable import Destroyable
from model.positionable import Positionable
from model.idgen import new_id
from abc import ABCMeta, abstractmethod

class Building(GameObject, Destroyable, Positionable, Nameable, Ownable, metaclass=ABCMeta):
    def __init__(self, building_id=-1, building_type="none", usable = False, *args, **kwargs):
        super(Building, self).__init__(*args, **kwargs)
        self._building_id = building_id if building_id != -1 else new_id()
        self._building_type = building_type
        self._usable = usable

    @property
    def building_id(self):
        return self._building_id

    @property
    def building_type(self):
        return self._building_type

    @property
    def usable(self):
        """wheter the building is usable. This is set to true if the building has been finished"""
        return self._usable

    @abstractmethod
    def max_health(self):
        """returns max health the building can have. This is also the health value at which is building is finished"""
        pass

    def storage_location(self):
        return "{0}/buildings/building-{1}.json".format(Ownable.storage_location(self), self.building_id)

    def symlinks(self):
        return [ "{0}/buildings/unit-{1}.json".format(Positionable.storage_location(self), self.building_id)
               , "{0}/buildings/by-type/{1}/unit-{2}.json".format(Ownable.storage_location(self), self.building_type, self.building_id)
               ]
