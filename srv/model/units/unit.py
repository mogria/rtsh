from model.gameobject import GameObject
from model.abilities.nameable import Nameable
from model.abilities.ownable import Ownable
from model.abilities.destroyable import Destroyable
from model.abilities.moveable import Moveable
from model.idgen import new_id

class Unit(GameObject):
    def __init__(self, unit_type, unit_id=-1, *args, **kwargs):
        super(Unit, self).__init__("unit", *args, **kwargs)
        self._unit_id = unit_id if unit_id != -1 else new_id()
        self._unit_type = unit_type

    @property
    def unit_id(self):
        return self._unit_id

    @property
    def unit_type(self):
        return self._unit_type

    def initial_abilities(self):
        return [ Nameable()
               , Ownable(owner=None)
               , Destroyable()
               , Moveable()
               ]

    def storage_location(self):
        ownable_location = self.ability("ownable").base_storage_location()
        return "{0}/units/unit-{1}.json".format(ownable_location, self.unit_id)

    def symlinks(self):
        moveable_location = self.ability("moveable").base_storage_location()
        ownable_location = self.ability("ownable").base_storage_location()
        return [ "{0}/units/unit-{1}.json".format(moveable_location, self.unit_id)
               , "{0}/units/by-type/{1}/unit-{2}.json".format(ownable_location, self.unit_type, self.unit_id)
               ]
