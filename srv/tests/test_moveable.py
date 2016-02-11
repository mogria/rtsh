import unittest
from model.abilities.moveable import Moveable

class MoveableTest(unittest.TestCase):
    def setUp(self):
        self.moveable = Moveable(move_speed = 2, position = (5, 5))

    def test_move_speed(self):
        self.assertEquals(2, self.moveable.move_speed)

    def test_move_target(self):
        self.assertEquals(None, self.moveable.move_target)
        self.moveable.move_target = (1,1)
        self.assertEquals((1,1), self.moveable.move_target)

    def test_pathfind_next_move(self):
        # no move target
        self.assertEquals((0, 0), self.moveable.pathfind_next_move())

        # nearby fields
        self.moveable.move_target = (4,5)
        self.assertEquals((-1, 0), self.moveable.pathfind_next_move())
        self.moveable.move_target = (6,5)
        self.assertEquals((1, 0), self.moveable.pathfind_next_move())
        self.moveable.move_target = (5,6)
        self.assertEquals((0, 1), self.moveable.pathfind_next_move())
        self.moveable.move_target = (5,4)
        self.assertEquals((0, -1), self.moveable.pathfind_next_move())

        # multiple fields on one coordinate
        self.moveable.move_target = (1,5)
        self.assertEquals((-1, 0), self.moveable.pathfind_next_move())
        self.moveable.move_target = (5,8)
        self.assertEquals((0, 1), self.moveable.pathfind_next_move())

        # multiple fields, two coordinates
        self.moveable.move_target = (1,4)
        self.assertEquals((-1, 0), self.moveable.pathfind_next_move())
        self.moveable.move_target = (4,8)
        self.assertEquals((0, 1), self.moveable.pathfind_next_move())

        # same distance on both coordinates
        self.moveable.move_target = (4,6)
        # repeat this, because random value out of two possibilities is chosen
        for x in range(100):
            self.moveable.move_target = (4,6)
            move = self.moveable.pathfind_next_move()
            self.assertTrue(move == (0, 1) or move == (-1, 0))

            self.moveable.move_target = (8,2)
            move = self.moveable.pathfind_next_move()
            self.assertTrue(move == (1, 0) or move == (0, -1))
