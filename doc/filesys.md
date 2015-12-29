# File System Layout

Because this game runs from within a bash shell and is in perfect harmony with the UNIX philosophy a lot of things are file based in this game.

## User Files (`$HOME`)
Every player is a user within his own? (maybe have single container for all users?) docker container.

As a user you operate within your `$HOME` directory. Your home directory then contains some other files.

### Unit Files (`$HOME/units`)

This folder contains a file for each unit you own.

### Building Files (`$HOME/buildings`)

This folder contains a file for every building you own.

### Groups (`$HOME/groups`)

This folder contains a folder with symlinks to every unit (buildings too?) in a group.

## World Files

All the files related to the game world you play in are stored in `/world`

### Map `/world/mapinfo`

Contains some info about the map. Size, name and the like. (split into multiple files?)

### Tile (`/world/tiles/$x/$y`)

The map is a 2D grid. Each cell of this grid is called a tile. For each tile there is a folder with the name of it's coordinates. This folder then contains files specific to this tile.

Every tile folder should have the following files

  * `terrain.json` - Contains info about what kind of terrain this tile is (forest, snow, grass, ...)
  * `units/` - Folder with a symlink to every unit in the `$HOME/units` of the respective players
  * `building` . A symlink to the building in $HOME/building of the respective player, *(optional)*

## Open questions:

 * share a single docker container for all users?
 * can you point to your enemies files?
 * how is the game board represented?
