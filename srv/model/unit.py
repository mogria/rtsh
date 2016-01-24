from model.gameobject import GameObject
from model.nameable import Nameable
from model.ownable import Ownable
from model.destroyable import Destroyable
from model.moveable import Moveable
from model.builder import Builder
from model.attacker import Attacker
from model.idgen import new_id

def isbuilder(unit):
    return isinstance(unit, Builder)

def isfighter(unit):
    return isinstance(unit, Attacker)

class Unit(GameObject, Destroyable, Moveable, Nameable, Ownable):
    def __init__(self, unit_id=-1, unit_type="none", *args, **kwargs):
        super(Unit, self).__init__(*args, **kwargs)
        self._unit_id = unit_id if unit_id != -1 else new_id()
        self._unit_type = unit_type

    @property
    def unit_id(self):
        return self._unit_id

    @property
    def unit_type(self):
        return self._unit_type

    def storage_location(self):
        return "{0}/units/unit-{1}.json".format(Ownable.storage_location(self), self.unit_id)

    def symlink_source_location(self):
        return "{0}/units/unit-{1}.json".format(Positionable.storage_location(self), self.unit_id)
