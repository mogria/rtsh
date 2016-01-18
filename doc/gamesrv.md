# The Game Server

The game server is responsible for executing the commands every player has run and keep the game moving!

## The Tick

A tick is the smallest time unit in the game. Every tick the game server sees what stuff there is to do (move units, create units, handle resources).

During a tick the server needs to do the following stuff in this order:

    * Move all units that need to be moved
    * Execute all attacks. If an units or buildings health falls below 0 don't remove it yet.
    * Remove all dead units and buildings.
    * Spawn all new units.
