#!/bin/bash
# build all docker containers from the source, so you don't need to pull
# them with the update.sh script

# pass arguments to this script file to the `docker build` command later
BUILD_ARGS=("$@")

SOURCE_LOCATION="$(cd "$(dirname "$0")" && pwd)"
. "$SOURCE_LOCATION/func.sh"

build() {
    echo " * Building $1"
    docker build -t "$1" "${BUILD_ARGS[@]}" "$SOURCE_LOCATION/$2"
}

build mogria/rtsh-srv srv && \
build mogria/rtsh-wetty-cli wetty-cli/ && \
build mogria/rtsh-base-world worlds/

if [ "$?" -ne 0 ]; then
    echo "E: build failed"
    exit 1
fi

# build all worlds
export -f build # export needed for xargs to find the build() function
export SOURCE_LOCATION
get_worlds | xargs -n1 -I '{}' bash -c "build 'mogria/rtsh-world-{}' 'worlds/{}'"
