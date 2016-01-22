import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

from commands.cheatCreateUnitCommand import CheatCreateUnitCommand


class CheatCreateUnitCommandTest(unittest.TestCase):
    def test_isValid_Only2Args_NotValid(self):
        expected = False
        only_2_args = [1, 2]
        result = CheatCreateUnitCommand.isValid(only_2_args)
        self.assertEqual(expected, result)

    def test_isValid_3Args_Valid(self):
        expected = True
        valid_args = ["swordfighter", 1, 2]
        result = CheatCreateUnitCommand.isValid(valid_args)
        self.assertEqual(expected, result)

    @patch("commands.cheatCreateUnitCommand.os.symlink")
    @patch("commands.cheatCreateUnitCommand.UnitFactory")
    @patch("commands.cheatCreateUnitCommand.Storage")
    def test_execute_callsStorageWrite(self, storage_class_mock, unit_factory_mock, symlink_method_mock):
        storage_mock = MagicMock()
        storage_class_mock.return_value = storage_mock

        unit_mock = MagicMock()
        unit_factory_mock.return_value = unit_mock

        args = ["swordfighter", 2, 3]
        sut = CheatCreateUnitCommand("playername", *args)
        sut.execute()

        unit_factory_mock.assert_called_once_with("swordfighter", owner="playername", position=(2, 3))
        storage_mock.write.assert_called_once_with(unit_mock)

    @patch("commands.cheatCreateUnitCommand.os.symlink")
    @patch("commands.cheatCreateUnitCommand.UnitFactory")
    @patch("commands.cheatCreateUnitCommand.Storage")
    def test_execute_createsSymlink(self, storage_class_mock, unit_factory_mock, symlink_method_mock):
        storage_mock = MagicMock()
        storage_class_mock.return_value = storage_mock

        unit_mock = MagicMock()
        expected_storage_location = "/someDir/someOtherDir/file.json"
        unit_mock.storage_location.return_value = expected_storage_location
        unit_factory_mock.return_value = unit_mock

        args = ["swordfighter", 2, 3]
        sut = CheatCreateUnitCommand("playername", *args)
        sut.execute()

        expected_symlink_location = "/world/2/3/units/file.json"
        symlink_method_mock.assert_called_once_with(expected_storage_location, expected_symlink_location)
