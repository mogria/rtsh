from model.gameobject import GameObject

class World(GameObject):
    def __init__(self, name = "none", size = [-1, -1], num_players = 0, start_positions = [], terrain_generator = "none", seed = -1):
        super(World, self).__init__("world")
        self._name = name
        self._size = size
        self._num_players = num_players
        self._start_positions = start_positions
        self._terrain_generator = terrain_generator
        self._seed =  seed

    @property
    def name(self):
        return self._name

    @property
    def size(self):
        return self._size

    @property
    def num_players(self):
        return self._num_players

    @property
    def start_positions(self):
        return self._start_positions

    @property
    def terrain_generator(self):
        return self._terrain_generator

    @property
    def seed(self):
        return self._seed

    def storage_location(self):
        return "/world/world.json"
