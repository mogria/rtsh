from model.gameobject import GameObject


class World(GameObject):
    STORAGE_LOCATION = "/world/world.json"
    def __init__(self, name="none", size=[-1, -1], max_players=0, start_coordinates=[], terrain_generator="none", seed=-1):
        super(World, self).__init__("world")
        self._name = name
        self._size = (int(size[0]), int(size[1]))
        self._max_players = max_players
        self._start_coordinates = start_coordinates
        self._terrain_generator = terrain_generator
        self._seed = seed

    @property
    def name(self):
        return self._name

    @property
    def size(self):
        return self._size

    @property
    def max_players(self):
        return self._max_players

    @property
    def start_coordinates(self):
        return self._start_coordinates

    @property
    def terrain_generator(self):
        return self._terrain_generator

    @property
    def seed(self):
        return self._seed

    def storage_location(self):
        return World.STORAGE_LOCATION

    def symlinks(self):
        # no symlinks needed
        return []
