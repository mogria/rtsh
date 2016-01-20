import unittest

from commands.commandFactory import createCommandClass
from commands.cheatCreateUnitCommand import CheatCreateUnitCommand
from commands.invalidGameCommandError import InvalidGameCommandError


class CommandFactoryTest(unittest.TestCase):
    def test_createCommandClass_NoValidCommand_RaisesException(self):
        emptyList = []
        with self.assertRaises(InvalidGameCommandError):
            createCommandClass("notImplementedCommandName", emptyList)

    def test_createCommandClass_ValidCommandNameButNotArgs_RaisesException(self):
        emptyList = []
        with self.assertRaises(InvalidGameCommandError):
            createCommandClass("cheat_create_unit", emptyList)

    def test_createCommandClass_CheatCreateUnitCommand_ReturnsCommand(self):
        validArgs = ["swordfighter", 1, 2]
        command = createCommandClass("cheat_create_unit", validArgs)
        self.assertIsInstance(command, CheatCreateUnitCommand)
