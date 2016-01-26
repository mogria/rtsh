#!/bin/bash
LOC="$(readlink -f "$(dirname "${BASH_SOURCE[0]}")")"
echo "building container ... "
echo "If you run this script the first time, this may take a while: "
docker build --quiet -t mogria/rtsh-srv-test -f "$LOC/Dockerfile_test" "$LOC"
docker run --rm -i -v "$LOC:/gamesrv:rw" mogria/rtsh-srv-test
