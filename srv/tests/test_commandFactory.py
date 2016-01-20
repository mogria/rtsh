import unittest

import commands.commandFactory
from commands.cheatCreateUnitCommand import CheatCreateUnitCommand
from commands.invalidGameCommandError import InvalidGameCommandError

class CommandFactoryTest(unittest.TestCase):

	def test_createCommandClass_NoValidCommand_RaisesException(self):
		emptyList = []
		with self.assertRaises(InvalidGameCommandError):
			commands.commandFactory.createCommandClass("notImplementedCommandName", emptyList)

	def test_createCommandClass_ValidCommandNameButNotArgs_RaisesException(self):
		emptyList = []
		with self.assertRaises(InvalidGameCommandError):
			commands.commandFactory.createCommandClass("cheat_create_unit", emptyList)

	def test_createCommandClass_CheatCreateUnitCommand_ReturnsCommand(self):
		validArgs = [1, 2, 3]
		command = commands.commandFactory.createCommandClass("cheat_create_unit", validArgs)
		self.assertIsInstance(command, CheatCreateUnitCommand)
