# Commands

These commands are provided within the docker container and can be used to control your units and buildings. Every commands is issued to the Game Server and evaluated on the next tick.

## `select $X $Y`

Select a location. Every command after this command is then issued on the selected location.

## `move $UNIT [$X $Y]`

Move a unit to a specific location.

## `build $BUILDERUNIT $BUILDINGNAME? [$X $Y]`

Build a building on a specific location with a specific builder unit.

## `group $UNITS...`

Create a group of units.
