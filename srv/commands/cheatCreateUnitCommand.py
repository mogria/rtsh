import os

from commands.baseCommand import BaseCommand
from model.storage import Storage
import model.unitfactory
from model.unitfactory import UnitFactory


class CheatCreateUnitCommand(BaseCommand):
    def __init__(self, player_name, unit_type, x, y):
        super().__init__("CheatCreateUnit")
        self._player_name = player_name
        self._unit_type = unit_type
        self._x = int(x)
        self._y = int(y)

    def execute(self):
        super().execute()

        u = UnitFactory(self._unit_type, owner=self._player_name, position=(self._x, self._y))
        path = u.storage_location()
        s = Storage(path)
        s.write(u)

        unit_name = path.split("/")[-1]
        symlink_location = "/world/{x}/{y}/units/{unitName}".format(x=self._x, y=self._y, unitName=unit_name)
        os.symlink(path, symlink_location)

        msg = "created unit {unit} and saved to {path}".format(unit=self._unit_type, path=path)
        print(msg)

    @classmethod
    def isValid(cls, args):
        super().isValid(args)
        if len(args) == 3 and args[0] in model.unitfactory.UNIT_TYPES:
            return True
        else:
            return False
