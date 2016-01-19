import unittest
import tempfile
from model.storage import Storage
from model.tile import Tile
from model.world import World

class StorageTest(unittest.TestCase):
    def setUp(self):
        self.tempfile = tempfile.mkstemp()[1]
        self.storage = Storage(self.tempfile)
        self.tile = Tile("grass", [1, 2])
        self.world = World("name", [7, 8], 2, [[1, 1], [6, 6]])

    def test_initialisation_by_object(self):
        tile = Tile("grass", [0, 0])
        storage = Storage(tile)
        storage.write(tile)
        tile2 = storage.read()
        self.assertEquals("grass", tile2.terrain())

    def test_write_tile(self):
        self.storage.write(self.tile)

    def test_read_tile(self):
        self.storage.write(self.tile)
        new_tile = self.storage.read()
        self.assertEquals(new_tile.terrain, self.tile.terrain)
        self.assertEquals(new_tile.position, self.tile.position)

    def test_write_world(self):
        self.storage.write(self.world)

    def test_read_world(self):
        self.storage.write(self.world)
        new_world = self.storage.read()
        self.assertEquals(new_world.name, self.world.name)
        self.assertEquals(new_world.size, self.world.size)
        self.assertEquals(new_world.num_players, self.world.num_players)

    def test_with_statement(self):
        t1 = Tile("grass", (0, 0))
        self.storage.write(t1)
        with Storage(self.tempfile) as tile:
            tile._terrain = "plain"
        t2 = self.storage.read()
        self.assertEquals("plain", t2.terrain)
        self.assertEquals(t1.position, t2.position)
