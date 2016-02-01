import glob
import time

from printWithFlush import p
from model.storage import Storage
from model.builder import Builder
from commandQueueProcessor import CommandQueueProcessor


TICK_INTERVAL_SEC = 1


class TickSystem(object):

    def __init__(self, players):
        self._players = players

    def process_user_commands(self):
        for player_name in self._players:
            cqp = CommandQueueProcessor(player_name)
            cqp.processCommands()

    def get_unit_files(self):
        return glob.glob("/world/**/unit-*.json", recursive=True)

    def units_tick(self):
        unit_files = self.get_unit_files()
        for f in unit_files:
            with Storage.from_file(f) as u:
                u.move()
                if isinstance(u, Builder):
                    u.build()

    def start(self):
        tick = 0
        while True:
            time.sleep(TICK_INTERVAL_SEC)
            p("tick ", tick)
            tick += 1
            self.process_user_commands()
            self.units_tick()
