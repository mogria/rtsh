import unittest
from model.abilities.destroyable import Destroyable

class DestroyableTest(unittest.TestCase):
    def setUp(self):
        self.destroyable = Destroyable(health = 50, armor_type = 'light')

    def test_invalid_armor_type(self):
        self.assertRaises(ValueError, Destroyable, health = 50, armor_type = 'something?')

    def test_armor_type(self):
        self.assertEquals('light', self.destroyable.armor_type)

    def test_health(self):
        self.assertEquals(50, self.destroyable.health)

    def test_get_attacked(self):
        self.destroyable.get_attacked(23, 'normal')
        self.assertEquals(27, self.destroyable.health)
        self.destroyable.get_attacked(2, 'pierce')
        self.assertEquals(26, self.destroyable.health)
        self.destroyable.get_attacked(2, 'sharp')
        self.assertEquals(22, self.destroyable.health)
        self.destroyable.get_attacked(2, 'blunt')
        self.assertEquals(20, self.destroyable.health)

    def test_is_destroyed(self):
        self.assertFalse(self.destroyable.is_destroyed())
        self.destroyable.get_attacked(49, 'normal')
        self.assertFalse(self.destroyable.is_destroyed())
        self.destroyable.get_attacked(1, 'normal')
        self.assertTrue(self.destroyable.is_destroyed())
        self.destroyable.get_attacked(1, 'normal')
        self.assertTrue(self.destroyable.is_destroyed())
