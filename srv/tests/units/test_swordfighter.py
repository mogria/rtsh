import unittest
from model.units.unit import Unit
from model.abilities.attacker import Attacker
from model.abilities.builder import Builder
from model.units.swordfighter import Swordfighter

class SlaveTest(unittest.TestCase):
    def setUp(self):
        self.swordfighter = Swordfighter()

    def test_instance(self):
        self.assertIsInstance(self.swordfighter, Unit)
        self.assertIsInstance(self.swordfighter.ability("attacker"), Attacker)
        self.assertNotIsInstance(self.swordfighter, Attacker)
        self.assertNotIsInstance(self.swordfighter, Builder)
