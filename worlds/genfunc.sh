#!/bin/bash

containsElement() {
    local e
    for e in "${@:2}"; do [[ "$e" == "$1" ]] && return 0; done
    return 1
}

set_attr_str() {
    jq --arg attr "$2" ".$1 = \$attr"
}

set_attr() {
    jq --argjson attr "$2" ".$1 = \$attr"
}

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
    if [ "$#" -lt 3 ]; then
        return 1
    fi

    output="$(new "world" | set_attr_str name "$1" | set_attr size "[$2, $3]")"
    
    if [ "$#" -ge 4 ]; then
        output="$(echo "$output" | set_attr_str terrain_generator "$4")"
    fi
    if [ "$#" -ge 5 ]; then
        output="$(echo "$output" | set_attr seed "$5")"
    fi
    echo "$output"
}

TERRAIN_TYPES=("grass" "desert" "woods" "plain")

terrain_generator_random() {
    terrain="${TERRAIN_TYPES[ $RANDOM % ${#TERRAIN_TYPES[@]} ] }"
    echo -n "$terrain"
}
