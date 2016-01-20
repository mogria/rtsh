from model.attacker import Attacker
from model.unit import Unit

class SwordfighterUnit(Unit, Attacker):
    def __init__(self, *args, **kwargs):
        kwargs['classname'] = 'unit'
        kwargs['unit_type'] = 'swordfighter'
        kwargs['health'] = 200
        kwargs['move_speed'] = 3
        kwargs['armor_type'] = 'medium'
        kwargs['attack_speed'] = 2
        kwargs['attack_type'] = 'sharp'
        kwargs['attack_range'] = 0
        kwargs['damage'] = 20

        super(SwordfighterUnit, self).__init__(*args, **kwargs)

    def give_name(self):
        return self._fake.name() + " of " + self._fake.city()
