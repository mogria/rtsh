#!/bin/bash

source "$(dirname "${BASH_SOURCE[0]}")/gameobjects.sh"
source "$(dirname "${BASH_SOURCE[0]}")/json.sh"

TERRAIN_TYPES=("grass" "desert" "woods" "plain")

terrain_generator_random() {
    terrain="${TERRAIN_TYPES[ $RANDOM % ${#TERRAIN_TYPES[@]} ] }"
    echo -n "$terrain"
}
