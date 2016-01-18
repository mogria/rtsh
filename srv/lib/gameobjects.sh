#!/bin/bash

source "$(dirname "${BASH_SOURCE[0]}")/array.sh"
source "$(dirname "${BASH_SOURCE[0]}")/json.sh"

new() {
    if [ "$#" -ne 1 ]; then
        return 1
    fi

    CLASSES=( "tile"  "world" "unit" "building" )
    if containsElement "$1" "${CLASSES[@]}"; then
        echo '{}' | set_attr_str class "$1"
        return 0
    fi
    return 1
}

new_tile() {
    if containsElement "$1" "${TERRAIN_TYPES[@]}"; then
        new "tile" | set_attr_str terrain "$1" | set_attr position "[$2, $3]"
        return 0
    fi
    return 1
}

new_world() {
    if [ "$#" -lt 4 ]; then
        return 1
    fi

    num_players="$4"
    output="$(new "world" | set_attr_str name "$1" | set_attr size "[$2, $3]" | set_attr max_players "$num_players")"

    coords=("${@:5:$((num_players * 2))}")
    json_coords=()
    i=0
    shift "${#coords[@]}"
    while [ "$i" -lt "$num_players" ]; do
        json_coords+=("[${coords[$((i * 2))]}, ${coords[$((i * 2 + 1))]}]")
        i="$((i + 1))"
    done

    output="$(echo "$output" | set_attr start_coordinates "[$(join ", " "${json_coords[@]}")]")"
    
    if [ "$#" -ge 5 ]; then
        output="$(echo "$output" | set_attr_str terrain_generator "$5")"
    fi
    if [ "$#" -ge 6 ]; then
        output="$(echo "$output" | set_attr seed "$6")"
    fi
    echo "$output"
}

UNIT_TYPES=("swordFighter")

new_unit() {
    if containsElement "$UNIT_TYPE" "${UNIT_TYPES[@]}"; then
        new "unit" | set_attr_str type "$UNIT_TYPE"
        return 0
    fi
    return 1
}
