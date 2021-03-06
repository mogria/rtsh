#!/bin/bash
# this script runs 3 docker containers
# - the game world
# - the game server
# - the wetty client which handles all the clients
#
# The following environment variables can affect the behaviour of this script:
#
# * RTSH_DEVELOP  
#   When set to a non-empty string the current source code in srv/ and wetty-cli/public
#   is mounted as a volume to the respective containers. Also 127.0.0.1 is the default
#   bind address for the wetty client.
# * SHOW_CLIENT  
#   When set to a non-empty string the output of the rtsh-wetty-cli container is shown
#   instead of the rtsh-srv container.
# * RTSH_BIND_ADDRESS
#   Set the ip the rtsh-wetty-cli container should bind to.
#   (This also overrides the 127.0.0.1 default of RTSH_DEVELOP)
# * RTSH_PORT
#   The port on which the rtsh-wetty-cli container should listen to
#   on the host part (default `80`)

echo "rtsh version 0.1, Copyright (C) 2016 by wtjerry, mogria, che4ter"
echo "rtsh comes with ABSOLUTELY NO WARRANTY; This is free software,"
echo "and you are welcome to redistribute it under certain conditions"

SOURCE_LOCATION="$(cd "$(dirname "$0")" && pwd)"
. "$SOURCE_LOCATION/func.sh"

if [ "$#" -lt 2 ]; then
    echo "Usage: $0 worldname playernames..."
    echo ""
    echo "You need to pass the worldname and at least 1 player name."
    echo "The worlds available are: "
    get_worlds | xargs -n1 printf " - %s"
    echo ""
    exit 1
fi

WORLD="$1"
shift
PLAYERS=("$@")

# stop & remove previous instances if running
docker stop --time 1 rtsh-srv rtsh-wetty-cli 2> /dev/null
docker rm rtsh-srv rtsh-wetty-cli 2> /dev/null

WORLD_CONTAINER_NAME="rtsh-world-$WORLD-$(date '+%Y-%m-%d_%H%M%S')"

# start the data container
docker run \
    --detach \
    --volume "/home" \
    --volume "/world" \
    --name "$WORLD_CONTAINER_NAME" \
    "mogria/rtsh-world-$WORLD" /bin/true

if [ "$?" -ne 0 ]; then
    echo "Couldn't start world '$WORLD'. Maybe something went wrong with docker or the image doesn't exist!"
    exit 1
fi

SRV_DOCKER_OPTS=
DEFAULT_BIND_ADDRESS="0.0.0.0"
RTSH_PORT="${RTSH_PORT:-80}"
CLI_DOCKER_OPTS="--detach"
if [ -n "$RTSH_DEVELOP" ]; then
    # if $RTSH_DEVELOP is set, mount the code inside srv/ of this project into the docker container, not the prebuilt code in the image
    echo "mounting source directories into containers"
    SRV_DOCKER_OPTS="$SRV_DOCKER_OPTS -v $SOURCE_LOCATION/srv:/gamesrv:ro"
    CLI_DOCKER_OPTS="$CLI_DOCKER_OPTS -v $SOURCE_LOCATION/wetty-cli/public:/app/public:rw"
    DEFAULT_BIND_ADDRESS="127.0.0.1"

    # run bower install so client-side javascript dependencies can also be served from
    # the host filesystem (you need bower installed for this) TODO: maybe use a docker container for this?
    echo "running 'bower install'"
    docker run -i --rm -v "$SOURCE_LOCATION/wetty-cli:/usr/src/app" --user $(id -u) mogria/rtsh-bower install

    # fix permissions for srv/commands
    chmod -R 755 $SOURCE_LOCATION/srv/commands
fi

start_client() {
    echo " * starting the wetty client"
    # start the client
    docker run -it \
        $CLI_DOCKER_OPTS \
        --publish ${RTSH_BIND_ADDRESS:-$DEFAULT_BIND_ADDRESS}:$RTSH_PORT:3000 \
        --volumes-from "$WORLD_CONTAINER_NAME" \
        --name rtsh-wetty-cli \
        --hostname "$WORLD" \
        mogria/rtsh-wetty-cli "${PLAYERS[@]}"
}

start_server() {
    echo " * starting the game server"
    docker run -it \
        $SRV_DOCKER_OPTS \
        --volumes-from "$WORLD_CONTAINER_NAME" \
        --name rtsh-srv \
        mogria/rtsh-srv "${PLAYERS[@]}"
}

# show the output of the client container instead of the server container 
# if the environment variable SHOW_CLIENT is set
if [ -n "$SHOW_CLIENT" ]; then
    CLI_DOCKER_OPTS="$(echo "$CLI_DOCKER_OPTS" | sed 's/--detach//g')"
    SRV_DOCKER_OPTS="--detach $SRV_DOCKER_OPTS"
    start_server
    start_client
else
    start_client
    start_server
fi



