from model.abilities.ability import Ability
from collections import Sequence
from pprint import pprint

class Positionable(Ability):
    def __init__(self, position = (-1, -1)):
        self._position = tuple(position)

    def ability_name(self):
        return "positionable"

    @property
    def position(self):
        """the position assigned to this object"""
        return self._position

    @position.setter
    def position(self, new_position):
        if not (isinstance(new_position, Sequence) and len(new_position) == 2
                and new_position[0] >= 0 and new_position[1] >= 0):
            raise ValueError("invalid position tuple. Must be two coordinates and not negative")
        self._position = tuple(new_position)

    def update(self, position = (-1, -1), *args, **kwargs):
        self.position = position

    def activate(self):
        pass

    def tick(self):
        pass

    def base_storage_location(self):
        """get the directory inside the world directory where this object is should be stored"""
        return "/world/{}/{}".format(*self.position)
