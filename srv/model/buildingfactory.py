from model.commonfactory import CommonFactory, is_valid_object_type
from model.buildings.castlebuilding import CastleBuilding

BUILDING_TYPES = {
    'castle': CastleBuilding, # main building, trains slaves, also acts as a warehouse
    'warehouse': None, # units which carry resources can deposit them here
    'house': None, # increases food limit
    'barracks': None, # trains squires and swordfighters
    'shooting_lane': None, # trains archers
    'stable': None, # trains cavalry
    'tower': None # can hit nearby enemy units
}

def BuildingFactory(building_type, *args, **kwargs):
    return CommonFactory("building", building_type, BUILDING_TYPES, *args, **kwargs)

def is_valid_building_type(building_type):
    return is_valid_object_type(building_type, BUILDING_TYPES)
