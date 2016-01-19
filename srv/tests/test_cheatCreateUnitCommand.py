import unittest
import sys
from unittest.mock import MagicMock
from unittest.mock import ANY
from unittest.mock import patch

sys.path.insert(0, '/gamesrv/commands')
sys.path.insert(0, '/gamesrv/model')
from cheatCreateUnitCommand import CheatCreateUnitCommand
from storage import Storage

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

	@patch("cheatCreateUnitCommand.Storage")
	def test_execute_callsStorageWrite(self, storageClassMock):
		m = MagicMock()
		storageClassMock.return_value = m

		args = [1, 2, 3]
		sut = CheatCreateUnitCommand(*args)
		sut.execute()

		#m.write.assert_called_once_with(ANY)
