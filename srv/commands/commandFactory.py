from cheatCreateUnitCommand import CheatCreateUnitCommand

class InvalidGameCommandError(Exception):
    def __init__(self, commandName, message, inner_exception = None):
        self.commandName = commandName
        self.message = message
        self.inner_exception = inner_exception


def createCommandClass(cmdName, *cmdArgs):
	commands = {
            "cheat_create_unit" : CheatCreateUnitCommand
        }
	
	if not cmdName in commands:
            raise InvalidGameCommandError(cmdName, "no command implemented with name: " + cmdName)
	
	return commands[cmdName](*cmdArgs)
