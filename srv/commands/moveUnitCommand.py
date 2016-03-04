import glob

from commands.baseCommand import BaseCommand
from model.storage import Storage
from model.world import World


class MoveUnitCommand(BaseCommand):
    def __init__(self, player_name, unit_id, x, y):
        super().__init__("MoveUnit", player_name)
        self._unit_id = int(unit_id)
        self._x = int(x)
        self._y = int(y)

    def execute(self):
        super().execute()

        print("pretending to doing stuff like moving units and so...")

        pattern = "/world/**/units/unit-{unit_id}.json".format(unit_id=self._unit_id)
        unit_path = glob.glob(pattern, recursive=True)[0]

        with Storage.from_file(unit_path) as unit:
            unit.move_target = (self._x, self._y)

    @classmethod
    def isValid(cls, player_name, args):
        super().isValid(args)

        if cls.has_correct_num_of_args(args) \
                and cls.is_valid_position(int(args[1]), int(args[2])) \
                and cls.is_existing_id_and_owned_by_player(int(args[0]), player_name):
            return True

        return False

    @classmethod
    def has_correct_num_of_args(cls, args):
        return len(args) == 3

    @classmethod
    def is_valid_position(cls, pos_x, pos_y):
        with Storage.from_file(World.STORAGE_LOCATION) as world:
            if 0 <= pos_x < world.size[0] and 0 <= pos_y < world.size[1]:
                return True

        return False

    @classmethod
    def is_existing_id_and_owned_by_player(cls, unit_id, player_name):
        pattern = "/home/{player_name}/units/unit-{unit_id}.json".format(player_name=player_name, unit_id=unit_id)
        print("pattern: " + pattern)
        matching_units = glob.glob(pattern, recursive=True)
        return len(matching_units) == 1
