#!/bin/sh
# this script updates all the docker containers (to the :latest tag)
# used by this project

SOURCE_LOCATION="$( cd "$(dirname "$0")" && pwd )"

docker pull mogria/rtsh-srv
docker pull mogria/rtsh-wetty-cli
docker pull mogria/rtsh-base-world

find "$SOURCE_LOCATION/worlds" \
    -mindepth 1 -maxdepth 1 \
    -type d -printf "mogria/rtsh-world-%f" \
        | xargs -n 1 docker pull 
