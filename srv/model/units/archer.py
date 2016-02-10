from model.units.unit import Unit
from model.abilities.attacker import Attacker

class Archer(Unit):
    def __init__(self, *args, **kwargs):
        self._register_abilitity(Attacker(15, 3, 'pierce', 1))
        kwargs['health'] = 150
        kwargs['move_speed'] = 4
        kwargs['armor_type'] = 'light'

        super(Archer, self).__init__('archer', *args, **kwargs)

    def give_name(self):
        return _fake.name()
