import glob

from commands.baseCommand import BaseCommand
from model.storage import Storage
from model.world import World


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

        pattern = "/world/**/unit-*-{unit_id}.json".format(unit_id=self._unit_id)
        unit_path = glob.glob(pattern, recursive=True)[0]

        with Storage(unit_path) as unit:
            unit.move_target = (self._x, self._y)

    @classmethod
    def isValid(cls, args):
        super().isValid(args)

        is_valid = False
        if len(args) == 3:
            arg_size_x = int(args[1])
            arg_size_y = int(args[2])

            with Storage(World.storage_location()) as world:
                if arg_size_x < world.size[0] and arg_size_y < world.size[1]:
                    is_valid = True

        return is_valid
