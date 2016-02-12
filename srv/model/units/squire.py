from model.units.unit import Unit
from model.abilities.attacker import Attacker
from model.abilities.builder import Builder
from model.abilities.destroyable import Destroyable
from model.abilities.moveable import Moveable

class Squire(Unit):
    def __init__(self, *args, **kwargs):
        super(Squire, self).__init__('squire', *args, **kwargs)

    def give_name(self, faker):
        return faker.first_name() + " the Squire"

    def initial_abilities(self):
        return super(Squire, self).initial_abilities() + [
                Destroyable(health=120, armor_type='medium')
              , Moveable(move_speed=3)
              , Attacker(damage=13, attack_type='sharp', attack_speed=3, attack_range=0)
              , Builder(build_speed=40, capacity=60)
              ]
