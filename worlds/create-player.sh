#!/bin/bash


if [ -z "$1" ]; then
    echo "Usage: $0 [-n] playername"
    echo "pass the -n option if you don't want to create the users home directory"
    exit 1
fi

OPTIND=1 # reset getopts

CREATE_HOME="--create-home"
while getopts "h?" opt; do
    case "$opt" in
        n) CREATE_HOME="-m"
           ;;
    esac
done

shift "$((OPTIND - 1))" # remove all non-positional arguments

NEWUID=9001

# TODO: all users are created without a password. We need some way
# to register users. so this script can get these passwords.


while ! cut -d: -f3 "/etc/passwd" | grep -E "^$NEWUID$"; do
    NEWUID="$((NEWUID + 1))"
done

useradd --password "" \
        $CREATE_HOME
        --uid "$NEWUID" \
        --home-dir "/home/$1" \
        --groups rtshplayers \
        "$1"

exit $?
