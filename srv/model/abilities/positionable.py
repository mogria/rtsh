from collections import Sequence

class Positionable(object):
    def __init__(self, position = (-1, -1), *args, **kwargs):
        super(Positionable, self).__init__(*args, **kwargs)
        if not (isinstance(position, Sequence) and len(position) == 2
                and position[0] >= 0 and position[1] >= 0):
            raise ValueError("invalid position tuple. Must be two coordinates and not negative")
        self._position = (position[0], position[1])

    @property
    def position(self):
        """the position assigned to this object"""
        return self._position

    def storage_location(self):
        """get the directory inside the world directory where this object is should be stored"""
        return "/world/{}/{}".format(*self.position)
