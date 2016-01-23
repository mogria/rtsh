from commands.invalidGameCommandError import InvalidGameCommandError
from commands.cheatCreateUnitCommand import CheatCreateUnitCommand
from commands.moveUnitCommand import MoveUnitCommand


def createCommandClass(player_name, cmd_name, cmd_args):
    commands = {
        "cheat_create_unit": CheatCreateUnitCommand,
        "move_unit": MoveUnitCommand
    }

    if cmd_name not in commands:
        raise InvalidGameCommandError(cmd_name, cmd_args, "no command implemented with name: " + cmd_name)

    is_valid = commands[cmd_name].isValid(cmd_args)
    if not is_valid:
        raise InvalidGameCommandError(cmd_name, "no command implemented with name: " + cmd_name)

    return commands[cmd_name](player_name, *cmd_args)
