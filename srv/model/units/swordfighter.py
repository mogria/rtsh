from model.units.unit import Unit
from model.abilities.attacker import Attacker
from model.abilities.destroyable import Destroyable
from model.abilities.moveable import Moveable

class Swordfighter(Unit):
    def __init__(self, *args, **kwargs):
        super(Swordfighter, self).__init__('swordfighter', *args, **kwargs)

    def give_name(self):
        return self._fake.name() + " of " + self._fake.city()

    def initial_abilities(self):
        return super(Swordfighter, self).initial_abilities() + [
                Destroyable(health=200, armor_type='medium')
              , Moveable(move_speed=3)
              , Attacker(damage = 20, attack_type='sharp', attack_speed=2, attack_range=0)
              ]
