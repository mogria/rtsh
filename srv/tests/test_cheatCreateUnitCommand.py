import unittest
import sys

sys.path.insert(0, '/gamesrv/commands')
from cheatCreateUnitCommand import CheatCreateUnitCommand

class CheatCreateUnitCommandTest(unittest.TestCase):

	def test_isValid_Only2Args_NotValid(self):
		expected = False
		only2Args = [1, 2]
		result = CheatCreateUnitCommand.isValid(only2Args)
		self.assertEqual(expected, result)

	def test_isValid_3Args_Valid(self):
		expected = True
		only2Args = [1, 2, 3]
		result = CheatCreateUnitCommand.isValid(only2Args)
		self.assertEqual(expected, result)
