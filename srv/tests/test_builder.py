import unittest
from model.castlebuilding import CastleBuilding
from model.builder import Builder

class BuilderTest(unittest.TestCase):
    def setUp(self):
        self.builder = Builder(build_speed = 41)
        self.building = CastleBuilding(position = (0, 0))

    def test_building_before_build(self):
        self.assertEquals(1, self.building.health)
        self.assertFalse(self.building.usable)

    def test_build_castle(self):
        # first build tick
        result = self.builder.build(self.building)
        self.assertFalse(result)
        self.assertEquals(42, self.building.health)
        self.assertFalse(self.building.usable)

        # second build tick
        result = self.builder.build(self.building)
        self.assertFalse(result)
        self.assertEquals(83, self.building.health)
        self.assertFalse(self.building.usable)

        # third build tick
        result = self.builder.build(self.building)
        self.assertTrue(result)
        self.assertEquals(self.building.max_health(), self.building.health)
        self.assertTrue(self.building.usable)
