import unittest

from commands.moveUnitCommand import MoveUnitCommand


class MoveUnitCommandTest(unittest.TestCase):
    def test_isValid_Only2Args_NotValid(self):
        expected = False
        only_2_args = [1, 2]
        result = MoveUnitCommand.isValid(only_2_args)
        self.assertEqual(expected, result)

    def test_isValid_3Args_Valid(self):
        expected = True
        valid_args = [99, 1, 2]
        result = MoveUnitCommand.isValid(valid_args)
        self.assertEqual(expected, result)
