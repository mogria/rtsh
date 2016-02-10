from model.units.unit import Unit
from model.abilities.attacker import Attacker

class Cavalry(Unit):
    def __init__(self, *args, **kwargs):
        self._register_ability(Attacker(30, 2, 'blunt', 0))
        kwargs['health'] = 300
        kwargs['move_speed'] = 1
        kwargs['armor_type'] = 'heavy'

        super(Cavalry, self).__init__('cavalry', *args, **kwargs)

    def give_name(self):
        return "Sir " + _fake.last_name() + "of" + _fake.city()
