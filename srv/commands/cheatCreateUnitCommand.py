from baseCommand import BaseCommand

class CheatCreateUnitCommand(BaseCommand):
	def __init__(self, unitType, x, y):
		super().__init__("CheatCreateUnit")
		self._unitType = unitType
		self._x = x
		self._y = y
	
	def execute(self):
		super().execute()
		print("pretending to doing stuff...")
