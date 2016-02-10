import unittest
from model.tile import Tile

class TileTest(unittest.TestCase):
    def setUp(self):
        self.t1 = Tile("grass", abilities: {'positionable': {'position': (1, 2)}})
        self.t2 = Tile("desert",abilities: {'positionable': {'position': [1, 2]}})

    def test_construct(self):
        self.assertEquals(self.t1.terrain, "grass")
        self.assertEquals(self.t2.terrain, "desert")
        self.assertEquals(self.t1.position, (1, 2))
        self.assertEquals(self.t2.position, (1, 2))
 
    def test_construct_invalid_terrain(self):
        self.assertRaises(ValueError, Tile, '', (1, 2))
        self.assertRaises(ValueError, Tile, "asdasdasdasdasd", (1, 2))

    def test_construct_invalid_position(self):
        self.assertRaises(ValueError, Tile, "grass", [])
        self.assertRaises(ValueError, Tile, "grass", 1)
        self.assertRaises(ValueError, Tile, "grass", [1])
        self.assertRaises(ValueError, Tile, "grass", (-1, 0))
        self.assertRaises(ValueError, Tile, "grass", (0, -1))
        self.assertRaises(ValueError, Tile, "grass", (-1, -1))

    def test_storage_location(self):
        self.assertEquals(self.t2.storage_location(), "/world/1/2/tile.json")
