from model.gameobject import GameObject
from model.ownable import Ownable
from model.nameable import Nameable
from model.destroyable import Destroyable
from model.positionable import Positionable
from model.idgen import new_id

class Building(GameObject, Destroyable, Positionable, Nameable, Ownable):
    def __init__(self, building_id=-1, building_type="none", *args, **kwargs):
        super(Building, self).__init__(*args, **kwargs)
        self._building_id = building_id if building_id != -1 else new_id()
        self._building_type = building_type

    @property
    def building_id(self):
        return self._building_id

    @property
    def building_type(self):
        return self._building_type

    def storage_location(self):
        return "{0}/buildings/building-{1}.json".format(Ownable.storage_location(self), self._building_type)
