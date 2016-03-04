import unittest
import tempfile
import os
from model.storage import Storage
from model.tile import Tile
from model.world import World
from model.unitfactory import UnitFactory
from model.dirty import dirty

class StorageTest(unittest.TestCase):

    def setUp(self):
        self.tempfile = tempfile.mkstemp()[1]
        self.tile = Tile("grass", [1, 2])
        self.tile_storage = Storage(self.tile)
        self.world = World("name", [7, 8], 2, [[1, 1], [6, 6]])
        self.world_storage = Storage(self.world)

    def test_initialisation_by_object(self):
        tile = Tile("grass", [0, 0])
        storage = Storage(tile)
        storage.write(make_dirty=True)
        tile2 = storage.read()
        self.assertEquals("grass", tile2.terrain)

    def test_write_tile(self):
        self.tile_storage.write(make_dirty=True)

    def test_read_tile(self):
        self.tile_storage.write(make_dirty=True)
        new_tile = self.tile_storage.read()
        self.assertEquals(new_tile.terrain, self.tile.terrain)
        self.assertEquals(new_tile.position, self.tile.position)

    def test_write_world(self):
        self.world_storage.write(make_dirty=True)

    def test_read_world(self):
        self.world_storage.write(make_dirty=True)
        new_world = self.world_storage.read()
        self.assertEquals(new_world.name, self.world.name)
        self.assertEquals(new_world.size, self.world.size)
        self.assertEquals(new_world.max_players, self.world.max_players)

    def test_with_statement(self):
        t1 = Tile("grass", (0, 0))
        storage = Storage(t1)
        storage.write(make_dirty=True)
        with Storage.from_file(t1.storage_location()) as tile:
            tile._terrain = "plain"
            tile.dirty()
        t2 = storage.read()
        self.assertEquals("plain", t2.terrain)
        self.assertEquals(t1.position, t2.position)

    def test_movable_gameobject_symlinks(self):
        unit = UnitFactory('slave', position=(0, 1), owner="johnny")
        storage = Storage(unit)
        self.assertFalse(os.path.exists(unit.storage_location()))
        for symlink in unit.symlinks():
            self.assertFalse(os.path.exists(symlink))
        storage.write()
        self.assertTrue(os.path.exists(unit.storage_location()))
        previous_symlinks = unit.symlinks()
        for symlink in previous_symlinks:
            self.assertTrue(os.path.exists(symlink))

        # new position should change a symlink
        unit._position = (2, 3)
        storage.write()
        removed_symlinks = set(previous_symlinks).difference(set(unit.symlinks()))
        for symlink in removed_symlinks:
            self.assertFalse(os.path.exists(symlink))

        symlinks_kept = set(unit.symlinks()).difference(set(previous_symlinks))
        for symlink in symlinks_kept:
            self.assertTrue(os.path.exists(symlink))

    def test_no_dirty_set(self):
        self.tile_storage.write() # no make_dirty
        self.assertFalse(os.path.exists(self.tile.storage_location()))
