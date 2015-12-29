# File Structures

This document describes how the different files used are layed out. Most of the files are in the .json format.

The `#` part within a file name gets replaced with an incrementing number. So that no files accidentally get overwritten.
This part also stored within the file as an `id`.

## `unit-#.json`

    {
        id: #,
        type: (UnitType)
    }

## terrain.json

    {
        type: (TerrainType)
    }

## building-#.json

    {
        id: #,
        type: (BuildingType)
    }

