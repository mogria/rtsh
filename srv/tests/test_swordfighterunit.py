import unittest
from model.unit import Unit
from model.attacker import Attacker
from model.builder import Builder
from model.swordfighterunit import SwordfighterUnit

class SlaveUnitTest(unittest.TestCase):
    def setUp(self):
        self.swordfighter = SwordfighterUnit(position = (0, 0))

    def test_instance(self):
        self.assertIsInstance(self.swordfighter, Unit)
        self.assertIsInstance(self.swordfighter, Attacker)
        self.assertNotIsInstance(self.swordfighter, Builder)
