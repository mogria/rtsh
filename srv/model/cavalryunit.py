from model.attacker import Attacker
from model.unit import Unit

class CavalryUnit(Unit, Attacker):
    def __init__(self, *args, **kwargs):
        kwargs['classname'] = 'unit'
        kwargs['unit_type'] = 'cavalry'
        kwargs['health'] = 300
        kwargs['move_speed'] = 1
        kwargs['armor_type'] = 'heavy'
        kwargs['attack_speed'] = 2
        kwargs['attack_type'] = 'blunt'
        kwargs['attack_range'] = 0
        kwargs['damage'] = 30

        super(CavalryUnit, self).__init__(*args, **kwargs)

    def give_name(self):
        return "Sir " + _fake.last_name() + "of" + _fake.city()
