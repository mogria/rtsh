#!/bin/bash

if [ "$#" -lt 2 ]; then
    echo "usage: $0 size_x size_y";
    exit 0
fi

SIZEX="$1"
SIZEY="$2"

TERRAIN_TYPES=("grass" "desert" "woods" "plain")

echo "generating World (${SIZEX}x$SIZEY)..."

for ((y = 0; x < SIZEY; y++)); do
    for ((x = 0; x < SIZEX; x++)); do
        mkdir -p "$x/$y"
        terrain="${TERRAIN_TYPES[ $RANDOM % ${#TERRAIN_TYPES[@]} ] }"
        cat > "$x/$y/terrain.json" <<terrainjson
{
    "class": "terrain",
    "type": "$terrain"
}
terrainjson
    done
done

echo "$((SIZEX * SIZEY)) tiles were generated"
