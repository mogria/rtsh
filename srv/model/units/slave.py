from model.abilities.destroyable import Destroyable
from model.abilities.moveable import Moveable
from model.abilities.builder import Builder
from model.units.unit import Unit

class Slave(Unit):
    def __init__(self, *args, **kwargs):
        super(Slave, self).__init__("slave", *args, **kwargs)

    def initial_abilities(self):
        return super(Slave, self).initial_abilities() + [
                 Destroyable(health=50, armor_type='light')
               , Moveable(move_speed=2)
               , Builder(build_speed=50, capacity=50)
               ]

    def give_name(self):
        return "Slave #{0}".format(self.unit_id)
