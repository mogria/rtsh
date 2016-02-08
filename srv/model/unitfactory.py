from model.commonfactory import CommonFactory
from model.units.slaveunit import SlaveUnit
from model.units.squireunit import SquireUnit
from model.units.swordfighterunit import SwordfighterUnit
from model.units.archerunit import ArcherUnit
from model.units.cavalryunit import CavalryUnit

UNIT_TYPES = {
    'slave': SlaveUnit,
    'squire': SquireUnit,
    'swordfighter': SwordfighterUnit,
    'archer': ArcherUnit,
    'cavalry': CavalryUnit
}

def UnitFactory(unit_type = "none",  *args, **kwargs):
    return CommonFactory("unit", unit_type, UNIT_TYPES, *args, **kwargs)
