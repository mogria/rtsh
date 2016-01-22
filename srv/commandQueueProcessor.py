import os

from printWithFlush import p
from util import getQueuePathFromPlayerName
from commands.commandFactory import createCommandClass
from commands.invalidGameCommandError import InvalidGameCommandError

class CommandQueueProcessor(object):

    def __init__(self, player_name):
        self._player_name = player_name

    def remove_new_line_characters(self, s):
        if s.endswith("\n"):
            s = s[:-1]
        return s

    def call_command(self, command_with_args):
        command_with_args = self.remove_new_line_characters(command_with_args)
        splitter = command_with_args.split(" ")
        cmd_name = splitter[0]
        cmd_args = splitter[1:]
        try:
            cmd_class = createCommandClass(cmd_name, cmd_args)
            cmd_class.execute()
        except InvalidGameCommandError:
            path_to_commands = "/gamesrv/commands"
            full_cmd_path = os.path.join(path_to_commands, cmd_name)
            p(full_cmd_path)
            if os.path.isfile(full_cmd_path):
                full_cmd_path_with_args = os.path.join(path_to_commands, command_with_args)
                p(os.system(full_cmd_path_with_args))

    def processCommands(self):
        p("player: ", self._player_name)
        queue_path = getQueuePathFromPlayerName(self._player_name)

        with open(queue_path, "r") as commandQueue:
            commands_with_args = commandQueue.readlines()
            for command in commands_with_args:
                self.call_command(command)
        with open(queue_path, "w") as commandQueue:
            commandQueue.truncate(0)
