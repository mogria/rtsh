from model.attacker import Attacker
from model.unit import Unit

class ArcherUnit(Unit, Attacker):
    def __init__(self, *args, **kwargs):
        kwargs['classname'] = 'unit'
        kwargs['unit_type'] = 'archer'
        kwargs['health'] = 150
        kwargs['move_speed'] = 4
        kwargs['armor_type'] = 'light'
        kwargs['attack_speed'] = 3
        kwargs['attack_type'] = 'pierce'
        kwargs['attack_range'] = 1
        kwargs['damage'] = 15

        super(ArcherUnit, self).__init__(*args, **kwargs)

    def give_name(self):
        return _fake.name()
