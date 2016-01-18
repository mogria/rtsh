from gameobject import GameObject

class Tile(GameObject):
    def __init__(self, terrain = "none", position = [-1, -1]):
        self._terrain = terrain
        self._position = position

    @property
    def terrain(self):
        return self._terrain

    @terrain.setter
    def terrain(self, new_terrain):
        self._terrain = new_terrain

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        self._position = new_position
