from model.commonfactory import CommonFactory
from model.castlebuilding import CastleBuilding

BUILDING_TYPES = {
    'castle': CastleBuilding, # main building, trains slaves, also acts as a warehouse
    'warehouse': None, # units which carry resources can deposit them here
    'house': None, # increases food limit
    'barracks': None, # trains squires and swordfighters
    'shooting_lane': None, # trains archers
    'stable': None, # trains cavalry
    'tower': None # can hit nearby enemy units
}

def BuildingFactory(building_type = "none",  *args, **kwargs):
    return CommonFactory("building", building_type, BUILDING_TYPES, *args, **kwargs)
