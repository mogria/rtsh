from commands.invalidGameCommandError import InvalidGameCommandError
from commands.cheatCreateUnitCommand import CheatCreateUnitCommand

def createCommandClass(cmdName, cmdArgs):

	commands = {
		"cheat_create_unit": CheatCreateUnitCommand
	}

	if cmdName not in commands:
		raise InvalidGameCommandError(cmdName, cmdArgs, "no command implemented with name: " + cmdName)
	
	isValid = commands[cmdName].isValid(cmdArgs)
	if not isValid:
		raise InvalidGameCommandError(cmdName, "no command implemented with name: " + cmdName)

	return commands[cmdName](*cmdArgs)
