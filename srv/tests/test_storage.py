import unittest
import tempfile
from model.storage import Storage
from model.tile import Tile
from model.world import World

class StorageTest(unittest.TestCase):

    def setUp(self):
        self.storage = Storage(tempfile.mkstemp()[1])
        self.tile = Tile("grass", [1, 2])
        self.world = World("name", [7, 8], 2, [[1, 1], [6, 6]])

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
