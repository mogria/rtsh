import unittest
import tempfile
from model.storage import Storage
from model.tile import Tile

class StorageTest(unittest.TestCase):
    def setUp(self):
        self.storage = Storage(tempfile.mkstemp()[1])
        self.tile = Tile("grass", [1, 2])

    def test_write(self):
        self.storage.write(self.tile)

    def test_read(self):
        self.storage.write(self.tile)
        new_tile = self.storage.read()
        self.assertEquals(new_tile.terrain, self.tile.terrain)
        self.assertEquals(new_tile.position, self.tile.position)
