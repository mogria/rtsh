#!/bin/bash
# this script updates all the docker containers (to the :latest tag)
# used by this project

. func.sh

docker pull mogria/rtsh-srv
docker pull mogria/rtsh-wetty-cli
docker pull mogria/rtsh-base-world

# pull all world containers
get_worlds | xargs -n1 printf "mogria/rtsh-world-%s" | xargs -n1 docker pull
