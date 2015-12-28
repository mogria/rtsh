#!/bin/bash
# build all docker containers from the source, so you don't need to pull
# them with the update.sh script

. func.sh

build() {
    echo " * Building $1"
    docker build -t "$1" "$(get_source_location)/$2"
}

build mogria/rtsh-srv srv
build mogria/rtsh-wetty-cli wetty-cli/
build mogria/rtsh-base-world worlds/

# build all worlds
export -f build # export needed for xargs to find the build() function
export -f get_source_location 
get_worlds | xargs -n1 -I '{}' bash -c "build 'mogria/rtsh-world-{}' 'worlds/{}'"
