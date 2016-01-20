from model.slaveunit import SlaveUnit
from model.squireunit import SquireUnit
from model.swordfighterunit import SwordfighterUnit
from model.archerunit import ArcherUnit
from model.cavalryunit import CavalryUnit

UNIT_TYPES = {
    'slave': SlaveUnit,
    'squire': SquireUnit,
    'swordfighter': SwordfighterUnit,
    'archer': ArcherUnit,
    'cavalry': CavalryUnit
}

class UnitConstructionError(Exception):
    def __init__(self, unit_type, message):
        super(UnitConstructionError, self).__init__("Construction error with unit_type '{0}': {1}".format(unit_type, message))


def UnitFactory(unit_type = "none",  *args, **kwargs):
    if not unit_type in UNIT_TYPES:
        raise UnitConstructionError(unit_type, "no such unit type")
    unit_class = UNIT_TYPES[unit_type]
    if unit_class == None:
        raise UnitConstructionError(unit_type, "unit not yet implemented")
    return unit_class(*args, **kwargs)
