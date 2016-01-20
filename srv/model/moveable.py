import numpy
import random
from model.positionable import Positionable

class Moveable(Positionable):
    def __init__(self, move_speed = 1, move_cycle = -1, move_target = None, *args, **kwargs):
        super(Moveable, self).__init__(*args, **kwargs)
        self._move_speed = move_speed
        self._move_cycle = move_cycle
        self._move_target = move_target

    @property
    def move_speed(self):
        return self._move_speed

    def reset_move_cycle(self):
        self._move_cycle = self.move_speed()

    def move(self):
        self._move_cycle -= 1
        if self._move_cycle <= 0:
            move = self.pathfind_next_move()
            if move[0] != 0 or move[1] != 0:
                self._position = numpy.add(self._position, self._move)
                # only reset move_cycle after we have actually moved
                self.reset_move_cycle()

    def pathfind_next_move(self):
        # simple path finding algorithm always taking the direct path
        # this only works as long as there are no obstacles on the map
        if self._move_target == None:
            return (0, 0)

        distance = numpy.subtract(self._move_target, self._position)
        if abs(distance[0]) > abs(distance[1]):
            # move along the x axis
            return (distance[0] / distance[0], 0)
        elif abs(distance[0]) < abs(distance[1]):
            # move along the y axis
            return (0, distance[1] / distance[1])
        else:
            # select  a random one
            n = random.randrange(1) == 0  
            chooser = (n, 1 - n)
            distance = numpy.divide(distance, distance)
            return numpy.multiply(distance, chooser)


