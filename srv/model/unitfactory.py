from model.commonfactory import CommonFactory
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

def UnitFactory(unit_type = "none",  *args, **kwargs):
    return CommonFactory("unit", unit_type, UNIT_TYPES, *args, **kwargs)
