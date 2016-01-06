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

## terrain.json

    {
        "class": "terrain",
        "type": (TerrainType)
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
        "size_x": (int),
        "size_y": (int),
        "terrain_generator": (String),
        "seed": (int)
    }
