from commands.baseCommand import BaseCommand


class MoveUnitCommand(BaseCommand):
    def __init__(self, player_name, unit_id, x, y):
        super().__init__("MoveUnit")
        self._player_name = player_name
        self._unit_id = int(unit_id)
        self._x = int(x)
        self._y = int(y)

    def execute(self):
        super().execute()

        print("pretending to doing stuff like moving units and so...")


    @classmethod
    def isValid(cls, args):
        super().isValid(args)
        if len(args) == 3:
            return True
        else:
            return False
