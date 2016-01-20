import abc

class BaseCommand(metaclass=abc.ABCMeta):
	
	def __init__(self, cmdName):
		self._cmdName = cmdName

	@abc.abstractmethod
	def execute(self):
		print("Executing", self._cmdName)

	@abc.abstractclassmethod
	def isValid(cls, args):
		print("Checking for validity of args", args)
