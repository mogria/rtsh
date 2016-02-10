from model.commonfactory import CommonFactory
from model.units.slave import Slave
from model.units.squire import Squire
from model.units.swordfighter import Swordfighter
from model.units.archer import Archer
from model.units.cavalry import Cavalry

UNIT_TYPES = {
    'slave': Slave,
    'squire': Squire,
    'swordfighter': Swordfighter,
    'archer': Archer,
    'cavalry': Cavalry
}

def UnitFactory(unit_type = "none",  *args, **kwargs):
    return CommonFactory("unit", unit_type, UNIT_TYPES, *args, **kwargs)
