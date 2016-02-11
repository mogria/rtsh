from model.units.unit import Unit
from model.abilities.attacker import Attacker
from model.abilities.destroyable import Destroyable
from model.abilities.moveable import Moveable

class Archer(Unit):
    def __init__(self, *args, **kwargs):
        super(Archer, self).__init__('archer', *args, **kwargs)

    def give_name(self):
        return _fake.name()

    def initial_abilities(self):
        return super(Archer, self).initial_abilities() + [
                Destroyable(health=150, armor_type='light')
              , Moveable(move_speed=4)
              , Attacker(damage=15, attack_type='pierce', attack_speed=3, attack_range=1)
              ]
