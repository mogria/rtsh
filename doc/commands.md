# Commands

These commands are provided within the docker container and can be used to control your units and buildings. Every commands is issued to the Game Server and evaluated on the next tick.

## `move [-q] $y/$x $UNITS...`

Move a unit to a specific location.
If `-q` is given queue up the command in the unit's command queue. if `-q` is not given all the current commands in the queue are discarded.

## `build [-q] $BUILDINGNAME [$y/$x] $BUILDERUNITS...`

Build a building on a specific location with a specific builder unit.
If `-q` is given queue up the command in the builderunit's command queue. if `-q` is not given all the current commands in the queue are discarded.

## `create [-q] [-n $AMOUNT] $UNITNAME $BUILDINGS...`
If `-q` is given queue up the command in the buildings's command queue. if `-q` is not given all the current commands in the queue are discarded.

## `group $UNITS...` (actually needed?)

Create a group of units.

# Utility Commands
These commands are, like all other commands, are provided within the client docker container. These commands however don't need to be executed on the server because they don't affect the game state. These commands are often just searching and filtering game objects.

## Filter commands

These utility commands filter through certain type of objects.
The objects to be filtered can be given through stdin as a collection of filenames delimited by `\n`.
If nothing is given through stdin all objects of a certain type are considered.
These commands output a collection of filenames delimited by `\n`, for which the filter criteria matched.
This way these commands can be used in
conjunction with other commands: 

 * by piping the output to an other filter command,
 * by piping the output to `xargs`
 * by using the output as command line arguments (e.g. `$(area...)`)

### `units`

Filter units on stdin (if no input given, all units), on a certain criteria.
If something on stdin is not a unit it is automatically filtered out of the output.

Maybe pass on arguments to `jq` for filtering by specific JSON attributes?

### `buildings`

Filter buildings on stdin (if no input given, all buildings), on a certain criteria.
If something on stdin is not a building it is automatically filtered out of the output.

Maybe pass on arguments to `jq` for filtering by specific JSON attributes?

### `tiles`

Filter tiles on stdin (if no input given, all tiles), on a certain criteria.
If something on stdin is not a tile it is automatically filtered out of the output.

Maybe pass on arguments to `jq` for filtering by specific JSON attributes?

### `area`

Filter through game objects (unit, buildings, tiles, ...?), make sure they're in a specific area. Only output game objects which are in this area.

This command either takes 1 or two positional arguments.

 * If `1` positional arguments are given in the form of `$y/$x`, only the tile at this exact coordinate is searched
 * If `2` positional arguments are given in the form of `$y1/$x1 $y2/$x2`, the rectangular area between
   these coordinates (the coordinates themselves included) are searched
