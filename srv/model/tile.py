from model.gameobject import GameObject
from model.abilities.positionable import Positionable

"""A single quadratic field on the world.
   It has a terrain and a position."""
class Tile(GameObject):
    """valid terrain strings"""
    VALID_TERRAINS = ["grass", "desert", "plain", "woods"]

    def __init__(self, terrain=None, *args, **kwargs):
        super(Tile, self).__init__("tile", *args, **kwargs)
        self.terrain = terrain

    @property
    def terrain(self):
        """the terrain of this tile"""
        return self._terrain

    @terrain.setter
    def terrain(self, new_terrain):
        if not new_terrain in Tile.VALID_TERRAINS:
            raise ValueError("invalid terrain '{0!s}', valid terrains are {1}".format(new_terrain, ', '.join(Tile.valid_terrains)))
            raise ValueError("invalid position tuple. Must be two coordinates and not negative")
        self._terrain = new_terrain


    def initial_abilities(self):
        return [Positionable()]

    def storage_location(self):
        """get the file name this tile should be stored at"""
        result = self.ability("positionable").base_storage_location() + "/tile.json"
        return result

    def symlinks(self):
        # no symlinks needed
        return []
