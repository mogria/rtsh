#!/bin/bash

echo args "$@"
for player in "$@"; do
    echo "creating player .... [$1]"
    /home/create-player.sh -n "$1"
done

exec node app.js -p 3000
