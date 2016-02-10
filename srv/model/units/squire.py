from model.units.unit import Unit
from model.abilities.attacker import Attacker
from model.abilities.builder import Builder

class Squire(Unit):
    def __init__(self, *args, **kwargs):
        self._register_abilitiy(Builder(40, 60))
        self._register_ability(Attacker(13, 3, 'sharp', 0))
        kwargs['health'] = 120
        kwargs['move_speed'] = 3
        kwargs['armor_type'] = 'medium'

        super(Squire, self).__init__('squire', *args, **kwargs)

    def give_name(self):
        return _fake.first_name() + " the Squire"
