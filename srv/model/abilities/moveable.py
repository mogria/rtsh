import numpy
import os
import random

from model.abilities.ability import Ability
from model.abilities.positionable import Positionable


class Moveable(Positionable):
    def __init__(self, move_speed=1, *args, **kwargs):
        super(Moveable, self).__init__(*args, **kwargs)
        self._move_speed = move_speed
        self._move_cycle = 0
        self._move_target = None

    def ability_name(self):
        return "moveable"

    @property
    def move_speed(self):
        return self._move_speed

    @property
    def move_cycle(self):
        return self._move_cycle

    @property
    def move_target(self):
        return self._move_target

    @move_target.setter
    def move_target(self, move_target):
        # TODO: check for valid coordinates
        self._move_target = move_target

    def update(self, move_cycle=-1, move_target=None, *args, **kwargs):
        super(Positionable, self).update(*args, **kwargs)
        self._move_cycle = move_cycle
        self._move_target = move_target

    def reset_move_cycle(self):
        self._move_cycle = self.move_speed

    def move(self):
        """move this object to the specified location set by move_target.
        A call to this function may do the following:
         - not move the object at all because the unit can't move this tick yet
         - not move the object at all because no move_target is specified
         - move the object by 1 field in the x or y coordinate
        This method should be called once, each tick, 
        so the movement speed of this object can be handled properly"""
        if self._move_cycle <= 0:
            move = self.pathfind_next_move()
            if move[0] != 0 or move[1] != 0:
                self.dirty()
                self._position = self.convert_back(numpy.add(self._position, move))
                # only reset move_cycle after we have actually moved
                self.reset_move_cycle()
            else:
                # reset move target
                self._move_target = None
        else:
            self._move_cycle -= 1

    def pathfind_next_move(self):
        """simple path finding algorithm, which always takes the direct path
        to the target. This only works as long as there are no obstacles
        on the map."""
        if self._move_target is None:
            return (0, 0)

        # check on which coordinate we need to walk longer
        # select a random one in case both coordinates distances are equal
        distance = numpy.subtract(self._move_target, self._position)
        absdistance = numpy.absolute(distance)
        is_x_longer = random.randrange(1)
        if   absdistance[0] > absdistance[1]: is_x_longer = 1
        elif absdistance[0] < absdistance[1]: is_x_longer = 0

        # (1, 0) if x coordinate is chosen, (0, 1) if y was chosen
        chooser = (is_x_longer, 1 - is_x_longer)
        # you can only move one field at maximum
        distance = numpy.sign(distance)
        # eliminate a coordinate
        distance = numpy.multiply(distance, chooser)
        return tuple(distance)

    def convert_back(self, nparray):
        pos1 = int(nparray[0])
        pos2 = int(nparray[1])
        t = (pos1, pos2)
        return t
