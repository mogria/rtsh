from model.gameobject import GameObject
from model.positionable import Positionable

"""A single quadratic field on the world.
   It has a terrain and a position."""
class Tile(GameObject, Positionable):
    """valid terrain strings"""
    valid_terrains = ["grass", "desert", "plain", "woods"]

    def __init__(self, terrain, *args, **kwargs):
        super(Tile, self).__init__("tile", *args, **kwargs)
        if not terrain in Tile.valid_terrains:
            raise ValueError("invalid terrain '{0!s}', valid terrains are {1}".format(terrain, ', '.join(Tile.valid_terrains)))
            raise ValueError("invalid position tuple. Must be two coordinates and not negative")
        self._terrain = terrain

    @property
    def terrain(self):
        """the terrain of this tile"""
        return self._terrain

    def storage_location(self):
        """get the file name this tile should be stored at"""
        return Positionable.storage_location(self) + "/tile.json"

    def symlinks(self):
        # no symlinks needed
        return []
