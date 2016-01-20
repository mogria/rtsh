from commands.baseCommand import BaseCommand
from model.storage import Storage
import model.unitfactory
from model.unitfactory import UnitFactory


class CheatCreateUnitCommand(BaseCommand):
    def __init__(self, unitType, x, y):
        super().__init__("CheatCreateUnit")
        self._unitType = unitType
        self._x = int(x)
        self._y = int(y)

    def execute(self):
        super().execute()

        u = UnitFactory(self._unitType, owner="foo", position=(self._x, self._y))
        path = u.storage_location()
        s = Storage(path)
        s.write(u)

        msg = "created unit {unit} and saved to {path}".format(unit=self._unitType, path=path)
        print(msg)

    @classmethod
    def isValid(cls, args):
        super().isValid(args)
        if len(args) == 3 and args[0] in model.unitfactory.UNIT_TYPES:
            return True
        else:
            return False
