#!/bin/bash
LOC="$(readlink -f "$(dirname "${BASH_SOURCE[0]}")")"
docker build --quiet -t mogria/rtsh-srv-test -f Dockerfile_test . > /dev/null
docker run --rm -i -v "$LOC:/gamesrv:rw" mogria/rtsh-srv-test
