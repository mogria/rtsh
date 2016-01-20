import unittest
from model.unit import Unit
from model.attacker import Attacker
from model.builder import Builder
from model.slaveunit import SlaveUnit

class SlaveUnitTest(unittest.TestCase):
    def setUp(self):
        self.slave = SlaveUnit(position = (0, 0))

    def test_instance(self):
        self.assertIsInstance(self.slave, Unit)
        self.assertIsInstance(self.slave, Builder)
        self.assertNotIsInstance(self.slave, Attacker)

    def test_values(self):
        self.assertRegex(self.slave.name, 'Slave #\d+')
        self.assertEquals(50, self.slave.health)
        self.assertEquals(2, self.slave.move_speed)
        self.assertEquals('light', self.slave.armor_type)
        self.assertEquals(50, self.slave.build_speed)
