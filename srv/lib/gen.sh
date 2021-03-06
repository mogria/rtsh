#!/bin/bash

LOC="$( cd "$(dirname "$0")" && pwd)"
. "$LOC/genfunc.sh"

if [ "$#" -lt 3 ]; then
    echo "usage: $0 worldname size_x size_y [terrain_generator]";
    exit 0
fi

WORLDNAME="$1"
SIZEX="$2"
SIZEY="$3"
PLAYERS="$4"
PLAYER_COORDS=( "${@:5:$((PLAYERS * 2))}" )
shift "${#PLAYER_COORDS[@]}"
TERRAIN_GENERATOR="${5:-random}"
SEED="$RANDOM"

echo "Generating world (${SIZEX}x$SIZEY) with '$TERRAIN_GENERATOR' generator (seed: $SEED) ..."

new_world "$WORLDNAME" "$SIZEX" "$SIZEY" "$PLAYERS" "${PLAYER_COORDS[@]}" "$TERRAIN_GENERATOR" "$SEED" > world.json

for ((y = 0; y < SIZEY; y++)); do
    for ((x = 0; x < SIZEX; x++)); do
        mkdir -p "$x/$y"
        terrain="$(terrain_generator_${TERRAIN_GENERATOR} "$x" "$y")"
        new_tile "$terrain" "$x" "$y" > "$x/$y/tile.json"
        mkdir "$x/$y/units"
    done
done

echo "$((SIZEX * SIZEY)) tiles were generated"
