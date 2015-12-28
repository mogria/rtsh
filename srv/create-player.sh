#!/bin/bash
if [ -z "$1" ]; then
    echo "Usage: $0 playername"
    exit 1
fi

# TODO: all users are created without a password. We need some way
# to register users. so this script can get these passwords.


useradd --password "" \
        --create-home  \
        --home-dir "/home/$1" \
        "$1"

exit $?
