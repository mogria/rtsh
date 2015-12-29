#!/bin/bash
# this script runs 3 docker containers
# - the game world
# - the game server
# - the wetty client which handles all the clients

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
docker stop rtsh-srv 2> /dev/null
docker stop rtsh-wetty-cli 2> /dev/null
docker rm rtsh-srv 2> /dev/null
docker rm rtsh-wetty-cli 2> /dev/null

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
CLI_DOCKER_OPTS="--publish 127.0.0.1:80:3000"
if [ -n "$RTSH_DEVELOP" ]; then
    # if $RTSH_DEVELOP is set, mount the code inside srv/ of this project into the docker container, not the prebuilt code in the image
    SRV_DOCKER_OPTS="-v $SOURCE_LOCATION/srv:/gamesrv:ro"
    CLI_DOCKER_OPTS="--publish 0.0.0.0:80:3000"
fi


echo " * starting the game server"
docker run \
    --detach \
    $SRV_DOCKER_OPTS \
    --volumes-from "$WORLD_CONTAINER_NAME" \
    --name rtsh-srv \
    mogria/rtsh-srv "${PLAYERS[@]}"

echo " * starting the wetty client"
# start the client
docker run \
    --detach \
    $CLI_DOCKER_OPTS \
    --volumes-from "$WORLD_CONTAINER_NAME" \
    --name rtsh-wetty-cli \
    mogria/rtsh-wetty-cli "${PLAYERS[@]}"

# show server output
docker attach rtsh-srv
