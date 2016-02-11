from model.units.unit import Unit
from model.abilities.attacker import Attacker
from model.abilities.destroyable import Destroyable
from model.abilities.moveable import Moveable

class Cavalry(Unit):
    def __init__(self, *args, **kwargs):
        super(Cavalry, self).__init__('cavalry', *args, **kwargs)

    def give_name(self):
        return "Sir " + _fake.last_name() + "of" + _fake.city()

    def initial_abilities(self):
        return super(Cavalry, self).initial_abilities() + [
                Destroyable(health=300, armor_type='heavy')
              , Moveable(move_speed=1)
              , Attacker(damage=30, attack_type='blunt', attack_speed=2, attack_range=0)
              ]
