import abc


class BaseCommand(metaclass=abc.ABCMeta):
    def __init__(self, cmd_name):
        self._cmd_name = cmd_name

    @abc.abstractmethod
    def execute(self):
        print("Executing", self._cmd_name)

    @abc.abstractclassmethod
    def isValid(cls, args):
        print("Checking for validity of args", args)
