#!/bin/bash
SOURCE_LOCATION="$( cd "$(dirname "$0")" && pwd )"

if [ "$#" -lt 2 ]; then
    echo "Usage: $0 worldname playernames..."
    echo ""
    echo "You need to pass the worldname and at least 1 player name."
    echo "The worlds available are: "
    find "$SOURCE_LOCATION/worlds" -mindepth 1 -maxdepth 1 -type d -printf " - %f\n"
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
if [ -n "$RTSH_DEVELOP" ]; then
    # if $RTSH_DEVELOP is set mount the actual code of this project into the docker container, not the prebuilt code in the image
    SRV_DOCKER_OPTS="-v $SOURCE_LOCATION/srv:/gamesrv:ro"
fi


echo " * starting the game server"
docker run \
    $SRV_DOCKER_OPTS \
    --volumes-from "$WORLD_CONTAINER_NAME" \
    --name rtsh-srv \
    mogria/rtsh-srv "${PLAYERS[@]}" \
    2> "$SOURCE_LOCATION/srv.log" > "$SOURCE_LOCATION/srv.log" &

echo " * starting the wetty client"
# start the client
docker run \
    --detach \
    --volumes-from "$WORLD_CONTAINER_NAME" \
    --name rtsh-wetty-cli \
    mogria/rtsh-wetty-cli

# show server output
tail -f "$SOURCE_LOCATION/srv.log"
