import unittest
from unittest.mock import ANY
from unittest.mock import patch

from commands.commandFactory import createCommandClass
from commands.invalidGameCommandError import InvalidGameCommandError
from commands.cheatCreateUnitCommand import CheatCreateUnitCommand
from commands.moveUnitCommand import MoveUnitCommand


class CommandFactoryTest(unittest.TestCase):
    def test_createCommandClass_NoValidCommand_RaisesException(self):
        empty_list = []
        with self.assertRaises(InvalidGameCommandError):
            createCommandClass(ANY, "notImplementedCommandName", empty_list)

    def test_createCommandClass_ValidCommandNameButNotArgs_RaisesException(self):
        empty_list = []
        with self.assertRaises(InvalidGameCommandError):
            createCommandClass(ANY, "cheat_create_unit", empty_list)

    def test_createCommandClass_CheatCreateUnitCommand_ReturnsCommand(self):
        valid_args = ["swordfighter", 1, 2]
        command = createCommandClass("playername", "cheat_create_unit", valid_args)
        self.assertIsInstance(command, CheatCreateUnitCommand)

    def test_createCommandClass_MoveUnitCommand_ReturnsCommand(self):
        with patch("commands.moveUnitCommand.Storage.from_file") as storage_mock:
            with patch("commands.moveUnitCommand.glob.glob") as glob_method_mock:
                world_mock = storage_mock.return_value.__enter__()
                world_mock.size = [8, 8]
                glob_method_mock.return_value = ["/somePath/unit-unitType-99.json"]

                valid_args = [99, 1, 2]
                command = createCommandClass("playername", "move_unit", valid_args)
                self.assertIsInstance(command, MoveUnitCommand)
