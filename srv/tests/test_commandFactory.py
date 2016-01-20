import unittest
import sys

sys.path.insert(0, '/gamesrv/commands')
import commandFactory
from cheatCreateUnitCommand import CheatCreateUnitCommand

class CommandFactoryTest(unittest.TestCase):

	def test_createCommandClass_NoValidCommand_RaisesException(self):
		emptyList = []
		with self.assertRaises(commandFactory.InvalidGameCommandError):
			commandFactory.createCommandClass("notImplementedCommandName", emptyList)

	def test_createCommandClass_ValidCommandNameButNotArgs_RaisesException(self):
		emptyList = []
		with self.assertRaises(commandFactory.InvalidGameCommandError):
			commandFactory.createCommandClass("cheat_create_unit", emptyList)

	def test_createCommandClass_CheatCreateUnitCommand_ReturnsCommand(self):
		validArgs = [1, 2, 3]
		command = commandFactory.createCommandClass("cheat_create_unit", validArgs)
		self.assertIsInstance(command, CheatCreateUnitCommand)
