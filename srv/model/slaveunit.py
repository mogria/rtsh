from model.builder import Builder
from model.unit import Unit

class SlaveUnit(Unit, Builder):
    def __init__(self, *args, **kwargs):
        kwargs['classname'] = 'unit'
        kwargs['unit_type'] = 'slave'
        kwargs['health'] = 50
        kwargs['move_speed'] = 2
        kwargs['armor_type'] = 'light'
        kwargs['build_speed'] = 50
        kwargs['capacity'] = 50
        super(SlaveUnit, self).__init__(*args, **kwargs)

    def give_name(self):
        return "Slave #{0}".format(self.unit_id)
