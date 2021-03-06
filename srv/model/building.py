from model.gameobject import GameObject
from model.ownable import Ownable
from model.nameable import Nameable
from model.destroyable import Destroyable
from model.positionable import Positionable
from model.idgen import new_id
from abc import ABCMeta, abstractmethod


class Building(GameObject, Destroyable, Positionable, Nameable, Ownable, metaclass=ABCMeta):
    def __init__(self, building_id=-1, building_type="none", *args, **kwargs):
        super(Building, self).__init__(classname="building", *args, **kwargs)
        self._building_id = building_id if building_id != -1 else new_id()
        self._building_type = building_type

    @property
    def building_id(self):
        return self._building_id

    @property
    def building_type(self):
        return self._building_type

    @property
    def usable(self):
        """whether the building is usable. This is true if the building has been finished"""
        is_usable = self.health >= self.max_health()
        return is_usable

    @abstractmethod
    def max_health(self):
        """returns max health the building can have. This is also the health value at which is building is finished"""
        pass

    def storage_location(self):
        return "{0}/buildings/building-{1}.json".format(Ownable.storage_location(self), self.building_id)

    def symlinks(self):
        return ["{0}/building/building.json".format(
                    Positionable.storage_location(self),
                    self.building_id),
                "{0}/buildings/by-type/{1}/building-{2}.json".format(
                    Ownable.storage_location(self),
                    self.building_type,
                    self.building_id)]
