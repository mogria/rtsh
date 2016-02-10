from model.units.unit import Unit
from model.abilities.attacker import Attacker

class Swordfighter(Unit):
    
    def __init__(self, *args, **kwargs):
        self._register_ability(Attacker(20, 2, 'sharp', 0))
        kwargs['health'] = 200
        kwargs['move_speed'] = 3
        kwargs['armor_type'] = 'medium'

        super(SwordfighterUnit, self).__init__('swordfighter', *args, **kwargs)

    def give_name(self):
        return self._fake.name() + " of " + self._fake.city()
