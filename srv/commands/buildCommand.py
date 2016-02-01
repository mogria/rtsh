from commands.baseCommand import BaseCommand
from model.buildingfactory import BuildingFactory, is_valid_building_type
from model.storage import Storage
from model.util import filterobject
from model.dirty import dirty
from model.builder import Builder

class BuildCommand(BaseCommand):
    def __init__(self, player_name, unit, building_type):
        super().__init__("Build")
        self._player_name = player_name
        self._unit = unit
        self._building_type = building_type

    def execute(self):
        super().execute()


        with Storage.from_file(self._unit) as unit:
            initial_attributes = filterobject(unit, ['position', 'owner'])
            building = BuildingFactory(self._building_type, **initial_attributes)
            Storage(building).write()
            unit._build_target = unit.position
            dirty(unit)

    @classmethod
    def isValid(cls, args):
        super().isValid(args)

        if cls.has_correct_num_of_args(args) \
            and cls.is_valid_builder(args[0]) \
            and cls.is_valid_building_type(args[1]):
            return True

        return False

    @classmethod
    def has_correct_num_of_args(cls, args):
        return len(args) == 2

    @classmethod
    def is_valid_builder(cls, unit):
        with Storage.from_file(unit) as u:
            return isinstance(u, Builder)

    @classmethod
    def is_valid_building_type(cls, building_type):
        return is_valid_building_type(building_type)
