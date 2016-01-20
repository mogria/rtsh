import unittest
from unittest.mock import MagicMock
from model.attacker import Attacker
from model.destroyable import Destroyable
from pprint import pprint

class AttackerTest(unittest.TestCase):
    def setUp(self):
        self.attacker = Attacker(damage = 20, attack_type = 'pierce', attack_speed = 2)
        self.destroyable = Destroyable(health = 1000, armor_type = 'normal')
        self.destroyable.get_attacked = MagicMock()

    def test_invalid_attack_type(self):
        self.assertRaises(ValueError, Attacker, damage = 10, attack_type = 'something?')

    def test_attack_type(self):
        self.assertEquals('pierce', self.attacker.attack_type)

    def test_damage(self):
        self.assertEquals(20, self.attacker.damage)

    def test_attack(self):
        self.attacker.attack(self.destroyable)
        # the destroyable should not get attacked
        # yet because the attacker has an attack speed of 2
        self.destroyable.get_attacked.assert_not_called()

        # this time the destroyable will actually get attacked
        self.attacker.attack(self.destroyable)
        self.assertEquals(1, self.destroyable.get_attacked.call_count)
        args = self.destroyable.get_attacked.call_args[0]
        self.assertGreaterEqual(22, args[0])
        self.assertLessEqual(18, args[0])
        self.assertEquals('pierce', args[1])

        # now it shouldn't get attacked again
        self.attacker.attack(self.destroyable)
        self.assertEquals(1, self.destroyable.get_attacked.call_count)

        # but now it should get called again
        self.attacker.attack(self.destroyable)
        self.assertEquals(2, self.destroyable.get_attacked.call_count)

