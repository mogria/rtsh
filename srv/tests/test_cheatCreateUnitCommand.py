import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

from commands.cheatCreateUnitCommand import CheatCreateUnitCommand


class CheatCreateUnitCommandTest(unittest.TestCase):
    def test_isValid_Only2Args_NotValid(self):
        expected = False
        only2Args = [1, 2]
        result = CheatCreateUnitCommand.isValid(only2Args)
        self.assertEqual(expected, result)

    def test_isValid_3Args_Valid(self):
        expected = True
        validArgs = ["swordfighter", 1, 2]
        result = CheatCreateUnitCommand.isValid(validArgs)
        self.assertEqual(expected, result)

    @patch("commands.cheatCreateUnitCommand.os.symlink")
    @patch("commands.cheatCreateUnitCommand.UnitFactory")
    @patch("commands.cheatCreateUnitCommand.Storage")
    def test_execute_callsStorageWrite(self, storageClassMock, unitFactoryMock, symLinkMethodMock):
        storageMock = MagicMock()
        storageClassMock.return_value = storageMock

        unitMock = MagicMock()
        unitFactoryMock.return_value = unitMock

        args = ["swordfighter", 2, 3]
        sut = CheatCreateUnitCommand(*args)
        sut.execute()

        unitFactoryMock.assert_called_once_with("swordfighter", owner="foo", position=(2, 3))
        storageMock.write.assert_called_once_with(unitMock)

    @patch("commands.cheatCreateUnitCommand.os.symlink")
    @patch("commands.cheatCreateUnitCommand.UnitFactory")
    @patch("commands.cheatCreateUnitCommand.Storage")
    def test_execute_createsSymlink(self, storageClassMock, unitFactoryMock, symLinkMethodMock):
        storageMock = MagicMock()
        storageClassMock.return_value = storageMock

        unitMock = MagicMock()
        expectedStorageLocation = "/someDir/someOtherDir/file.json"
        unitMock.storage_location.return_value = expectedStorageLocation
        unitFactoryMock.return_value = unitMock

        args = ["swordfighter", 2, 3]
        sut = CheatCreateUnitCommand(*args)
        sut.execute()

        expectedSymlinkLocation = "/world/2/3/units/file.json"
        symLinkMethodMock.assert_called_once_with(expectedStorageLocation, expectedSymlinkLocation)
