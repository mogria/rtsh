import unittest
from model.units.unit import Unit
from model.units.slave import Slave
from model.abilities.attacker import Attacker
from model.abilities.builder import Builder

class SlaveTest(unittest.TestCase):
    def setUp(self):
        self.slave = Slave(abilities={'ownable': {'owner': 'johnny'}})

    def test_instance(self):
        self.assertIsInstance(self.slave, Unit)
        self.assertIsInstance(self.slave.ability("builder"), Builder)
        self.assertNotIsInstance(self.slave, Builder)
        self.assertNotIsInstance(self.slave.ability("attacker"), Builder)
        self.assertNotIsInstance(self.slave, Attacker)

    def test_values(self):
        self.assertRegex(self.slave.name, 'Slave #\d+')
        self.assertEquals(50, self.slave.health)
        self.assertEquals(2, self.slave.move_speed)
        self.assertEquals('light', self.slave.armor_type)
        self.assertEquals(50, self.slave.build_speed)

    def test_storage_location(self):
        id = self.slave.unit_id
        self.assertEquals("/home/johnny/units/unit-{0}.json".format(id), self.slave.storage_location())
