import os
import subprocess
import shlex

from printWithFlush import p
from util import getQueuePathFromPlayerName
from commands.commandFactory import createCommandClass
from commands.invalidGameCommandError import InvalidGameCommandError


class CommandQueueProcessor(object):

    def __init__(self, player_name):
        self._player_name = player_name

    def processCommands(self):
        p("player: ", self._player_name)
        queue_path = getQueuePathFromPlayerName(self._player_name)

        with open(queue_path, "r") as commandQueue:
            commands_with_args = commandQueue.readlines()
            for command in commands_with_args:
                self.process_command(command)
        with open(queue_path, "w") as commandQueue:
            commandQueue.truncate(0)

    def process_command(self, command_with_args):
        command_with_args = self.remove_new_line_characters(command_with_args)
        splitter = shlex.split(command_with_args)
        cmd_workdir = splitter[0]
        cmd_name = splitter[1]
        cmd_args = splitter[2:]
        try:
            self.try_execute_python_command(cmd_workdir, cmd_name, cmd_args)
        except InvalidGameCommandError:
            self.try_execute_shell_command(cmd_workdir, cmd_name, cmd_args)

    def remove_new_line_characters(self, s):
        if s.endswith("\n"):
            s = s[:-1]
        return s

    def try_execute_python_command(self, cmd_workdir, cmd_name, cmd_args):
        prev_cwd = os.getcwd()
        os.chdir(cmd_workdir)
        cmd_class = createCommandClass(self._player_name, cmd_name, cmd_args)
        cmd_class.execute()
        os.chdir(prev_cwd)

    def try_execute_shell_command(self, cmd_workdir, cmd_name, cmd_args):
        path_to_commands = "/gamesrv/commands"
        full_cmd_path = os.path.join(path_to_commands, cmd_name)
        p("full_cmd_path:")
        p(full_cmd_path)
        if os.path.isfile(full_cmd_path):
            with subprocess.Popen(["/bin/bash", full_cmd_path, *cmd_args], cwd=cmd_workdir, stdout=subprocess.PIPE) as proc:
                try:
                    proc.wait(200)
                except subprocess.TimeoutExpired:
                    proc.terminate()
                finally:
                    print(proc.stdout.read())
