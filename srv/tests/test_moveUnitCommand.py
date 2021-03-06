import unittest
from unittest.mock import patch

from commands.moveUnitCommand import MoveUnitCommand


class MoveUnitCommandTest(unittest.TestCase):
    def test_isValid_Only2Args_NotValid(self):
        expected = False
        only_2_args = [1, 2]
        result = MoveUnitCommand.isValid("player1", only_2_args)
        self.assertEqual(expected, result)

    def test_isValid_targetPosOutOfBounds_NotValid(self):
        with patch("commands.moveUnitCommand.Storage.from_file") as storage_mock:
            world_mock = storage_mock.return_value.__enter__()
            world_mock.size = [8, 8]

            out_of_bound_pos_x = [1, 8, 2]
            result = MoveUnitCommand.isValid("player1", out_of_bound_pos_x)
            self.assertEqual(False, result)

            out_of_bound_pos_y = [1, 2, 8]
            result = MoveUnitCommand.isValid("player1", out_of_bound_pos_y)
            self.assertEqual(False, result)

    def test_isValid_3Args_Valid(self):
        with patch("commands.moveUnitCommand.Storage.from_file") as storage_mock:
            with patch("commands.moveUnitCommand.glob.glob") as glob_method_mock:
                world_mock = storage_mock.return_value.__enter__()
                world_mock.size = [8, 8]
                glob_method_mock.return_value = ["/home/player1/units/unit-unitType-99.json"]

                expected = True
                valid_args = [99, 1, 2]
                result = MoveUnitCommand.isValid("player1", valid_args)
                self.assertEqual(expected, result)

    def test_isValid_UnitNotOwned_NotValid(self):
        with patch("commands.moveUnitCommand.Storage.from_file") as storage_mock:
            with patch("commands.moveUnitCommand.glob.glob") as glob_method_mock:
                world_mock = storage_mock.return_value.__enter__()
                world_mock.size = [8, 8]
                glob_method_mock.return_value = []

                expected = False
                valid_args = [99, 1, 2]
                result = MoveUnitCommand.isValid("player1", valid_args)
                self.assertEqual(expected, result)

