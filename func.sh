#!/bin/bash

get_worlds() {
    find "$(cd "$(dirname "$0")" && pwd)/worlds" -mindepth 1 -maxdepth 1 -type d -printf "%f"
}
