import unittest
from model.commonfactory import ConstructionError
from model.unitfactory import UnitFactory, UNIT_TYPES
from model.slaveunit import SlaveUnit
from model.squireunit import SquireUnit
from model.swordfighterunit import SwordfighterUnit
from model.archerunit import ArcherUnit
from model.cavalryunit import CavalryUnit

class UnitFactoryTest(unittest.TestCase):
    def test_invalid_unit_type(self):
        self.assertRaises(ConstructionError, UnitFactory, 'notavalidunittype')

    def test_no_implementation_error(self):
        UNIT_TYPES['undefinedunit'] = None # let's hack in a unit which is not implemented
        self.assertRaises(ConstructionError, UnitFactory, 'undefinedunit')

    def test_construct_slave(self):
        self.assertIsInstance(UnitFactory('slave', position = (0, 0)), SlaveUnit)

    def test_construct_squire(self):
        self.assertIsInstance(UnitFactory('squire', position = (0, 0)), SquireUnit)

    def test_construct_swordfighter(self):
        self.assertIsInstance(UnitFactory('swordfighter', position = (0, 0)), SwordfighterUnit)

    def test_construct_archer(self):
        self.assertIsInstance(UnitFactory('archer', position = (0, 0)), ArcherUnit)

    def test_construct_cavalry(self):
        self.assertIsInstance(UnitFactory('cavalry', position = (0, 0)), CavalryUnit)
