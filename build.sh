#!/bin/bash
# build all docker containers from the source, so you don't need to pull
# them with the update.sh script

# exit immediately if any command in here fails
set -e

# pass arguments to this script file to the `docker build` command later
BUILD_ARGS=("$@")

SOURCE_LOCATION="$(cd "$(dirname "$0")" && pwd)"
cd "$SOURCE_LOCATION"

. "./func.sh"

build() {
    echo " * Building $1"
    if [ -z "$3" ]; then
        echo " $ docker build -t" "$1" "${BUILD_ARGS[@]}" "./$2"
        docker build -t "$1" "${BUILD_ARGS[@]}" "./$2"
    else
        echo " $ docker build -t" "$1" "${BUILD_ARGS[@]}" -f "./$2/$3" "./$2"
        docker build -t "$1" "${BUILD_ARGS[@]}" -f "./$2/$3" "./$2"
    fi
}

build mogria/rtsh-srv srv && \
build mogria/rtsh-wetty-cli wetty-cli/ && \
build mogria/rtsh-base-world "srv/lib"
build mogria/rtsh-srv-test srv Dockerfile_test
build mogria/rtsh-bower wetty-cli Dockerfile_bower

# build all worlds
export -f build # export needed for xargs to find the build() function
get_worlds | xargs -n1 -I '{}' bash -c "build 'mogria/rtsh-world-{}' '$WORLDS_DIR/{}'"
