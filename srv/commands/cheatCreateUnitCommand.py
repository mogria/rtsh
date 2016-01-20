from commands.baseCommand import BaseCommand
from model.storage import Storage

class CheatCreateUnitCommand(BaseCommand):

	def __init__(self, unitType, x, y):
		super().__init__("CheatCreateUnit")
		self._unitType = unitType
		self._x = x
		self._y = y
	
	def execute(self):
		super().execute()
		print("pretending to doing stuff...")
		#s = Storage(correctStorageHere)
		#u = Unit...
		#s.write(u)
	
	@classmethod
	def isValid(cls, args):
		super().isValid(args)
		if len(args) == 3:
			return True
		else:
			return False
