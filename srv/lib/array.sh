#!/bin/bash

containsElement() {
    local e
    for e in "${@:2}"; do [[ "$e" == "$1" ]] && return 0; done
    return 1
}

join() {
    local IFS="$1"
    shift
    echo "$*"
}

