#!/bin/bash

WORLDS_DIR=srv/lib/worlds
get_worlds() {
    find "$(cd "$(dirname "$0")" && pwd)/$WORLDS_DIR" -mindepth 1 -maxdepth 1 -type d -printf "%f"
}
