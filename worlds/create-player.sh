#!/bin/bash
if [ -z "$1" ]; then
    echo "Usage: $0 playername"
    exit 1
fi

NEWUID=9001

# TODO: all users are created without a password. We need some way
# to register users. so this script can get these passwords.


while ! cut -d: -f1 | grep -E "^$NEWUID\$"; do
    NEWUID="$((NEWUID + 1))"
done

useradd --password "" \
        --create-home  \
        --uid "$NEWUID"
        --home-dir "/home/$1" \
        --groups rtshplayers \
        "$1"

exit $?
