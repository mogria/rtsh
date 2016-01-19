from model.gameobject import GameObject
from collections import Sequence

"""A single quadratic field on the world.
   It has a terrain and a position."""
class Tile(GameObject):
    """valid terrain strings"""
    valid_terrains = ["grass", "desert", "plain", "woods"]

    def __init__(self, terrain, position):
        super(Tile, self).__init__("tile")
        if not terrain in Tile.valid_terrains:
            raise ValueError("invalid terrain '{0!s}', valid terrains are {1}".format(terrain, ', '.join(Tile.valid_terrains)))
        if not (isinstance(position, Sequence) and len(position) == 2
                and position[0] >= 0 and position[1] >= 0):
            raise ValueError("invalid position tuple. Must be two coordinates and not negative")
        self._terrain = terrain
        self._position = (position[0], position[1])

    @property
    def terrain(self):
        """the terrain of this tile"""
        return self._terrain

    @property
    def position(self):
        """the position of this tile on the world"""
        return self._position

    def storage_location(self):
        """get the file name this tile should be stored at"""
        return "/world/{}/{}/tile.json".format(*self._position)
