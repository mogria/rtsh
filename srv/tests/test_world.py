import unittest
from model.world import World

class WorldTest(unittest.TestCase):
    def test_storage_location(self):
        self.assertEquals(World("test").storage_location(), "/world/world.json")
