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

        self.attacker.randomized_damage = MagicMock(return_value = 21)

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
        self.destroyable.get_attacked.assert_called_once_with(21, 'pierce')

        # now it shouldn't get attacked again
        self.attacker.attack(self.destroyable)
        self.assertEquals(1, self.destroyable.get_attacked.call_count)

        # but now it should get called again
        self.attacker.attack(self.destroyable)
        self.assertEquals(2, self.destroyable.get_attacked.call_count)

    def test_randomized_damage(self):
        for x in range(100):
            attacker = Attacker(damage = 1000, attack_type = 'normal')
            randomized_damage = attacker.randomized_damage()
            self.assertGreaterEqual(1100, randomized_damage)
            self.assertLessEqual(900, randomized_damage)
