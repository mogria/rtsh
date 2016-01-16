# Units

This file describes what units types are available and what abilities they have.
Every unit has the common properties. Every builder unit is capable of collecting
resources and create buildings on the map.
Fighting units are able to destroy enemy units and buildings.
Some units may be both builder and fighting units.

## Common properties

 * `health`: when this drops to zero or below, the unit dies
 * `movespeed`: after how many ticks the unit can move.
 * `armortype`: how the unit is armored

## Builder unit properties

 * `buildspeed`: how much health is added to a building each tick, when creating or repairing a structure
 * `capacity`: how many resources the unit can carry.

## Fighting unit properties

 * `attackspeed`: after how many ticks the unit can attack.
 * `attacktype`: how the unit attacks
 * `attackrange`: how many fields away the unit can attack. `0` -> on the same field. `1` -> nearby fields (top, bottom, right, left).
 * `damage`: how much damage the unit deals

 
## armor types and attack types

| armor/attack | pierce | blunt | sharp |
|:-------------|:-------|:------|:------|
| heavy        |   200% |   50% |  100% |
| medium       |   100% |  200% |   50% |
| light        |    50% |  100% |  200% |

## Table of units

| Unit         | Slave   | Squire          | Swordfighter | Archer  | Cavalry |
|:-------------|:--------|:----------------|:-------------|:--------|:--------|
| Unit Type    | Builder | Builder/Fighter | Fighter      | Fighter | Fighter |
| Health       | 50      | 120             | 200          | 150     | 300     |
| Movespeed    | 2       | 3               | 3            | 4       | 1       |
| Armor Type   | light   | medium          | medium       | light   | heavy   |
| Buildspeed   | 50      | 40              | -            | -       | -       |
| Capacity     | 50      | 60              | -            | -       | -       |
| Attackspeed  | -       | 3               | 2            | 3       | 2       |
| Attack Type  | -       | sharp           | sharp        | pierce  | blunt   |
| Attack Range | -       | 0               | 0            | 1       | 0       |
| Damage       | -       | 13              | 20           | 15      | 30      |

