# File Structures

This document describes how the different files used are layed out. Most of the files are in the .json format.

The `#` part within a file name gets replaced with an incrementing number. So that no files acc"id"entally get overwritten.
This part also stored within the file as an `"id"`.

## `unit-#.json`

    {
        "class": "unit",
        "id": #,
        "type": (UnitType)
    }

## tile.json

    {
        "class": "tile",
        "terrain": (TerrainType)
        "size": [(int), (int)],
    }

## building-#.json

    {
        "class": "building",
        "id": #,
        "type": (BuildingType)
    }

## world.json

    {
        "class": "world",
        "size": [(int), (int)],
        "terrain_generator": (String),
        "seed": (int)
    }
