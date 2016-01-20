from model.gameobject import GameObject
from model.nameable import Nameable
from model.destroyable import Destroyable
from model.moveable import Moveable
from model.builder import Builder
from model.attacker import Attacker
from model.idgen import new_id

def isbuilder(unit):
    return isinstance(unit, Builder)

def isfighter(unit):
    return isinstance(unit, Attacker)

class Unit(GameObject, Destroyable, Moveable, Nameable):
    def __init__(self, unit_id=-1, owner="none", unit_type="none", *args, **kwargs):
        self._unit_id = unit_id if unit_id != -1 else new_id()
        self._owner = owner
        self._unit_type = unit_type
        super(Unit, self).__init__(*args, **kwargs)

    @property
    def unit_id(self):
        return self._unit_id

    @property
    def owner(self):
        return self._owner

    @property
    def unit_type(self):
        return self._unit_type

    def storage_location(self):
        return "/home/{0}/units/unit-{1}.json".format(self._owner, self._unit_type)
