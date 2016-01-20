from model.attacker import Attacker
from model.builder import Builder
from model.unit import Unit

class SquireUnit(Unit, Builder, Attacker):
    def __init__(self, *args, **kwargs):
        kwargs['classname'] = 'unit'
        kwargs['unit_type'] = 'squire'
        kwargs['health'] = 120
        kwargs['move_speed'] = 3
        kwargs['armor_type'] = 'medium'
        kwargs['build_speed'] = 40
        kwargs['capacity'] = 60
        kwargs['attack_speed'] = 3
        kwargs['attack_type'] = 'sharp'
        kwargs['attack_range'] = 0
        kwargs['damage'] = 13

        super(SquireUNit, self).__init__(*args, **kwargs)

    def give_name(self):
        return _fake.first_name() + " the Squire"
