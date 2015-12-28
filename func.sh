#!/bin/bash

get_source_location() {
    cd "$(dirname "$0")" && pwd
}

get_worlds() {
    find "$(get_source_location)/worlds" -mindepth 1 -maxdepth 1 -type d -printf "%f"
}
