#!/bin/bash


if [ -z "$1" ]; then
    echo "Usage: $0 [-n] playername"
    echo "pass the -n option if you don't want to create the users home directory"
    exit 1
fi

CREATE_HOME="--create-home"
if [ "$1" == "-n" ]; then
    CREATE_HOME="-M"
    shift
fi

NEWUID=9001

# TODO: all users are created without a password. We need some way
# to register users. so this script can get these passwords.


while cut -d: -f3 "/etc/passwd" | grep -E "^$NEWUID$"; do
    NEWUID="$((NEWUID + 1))"
done

useradd --password "*" \
        $CREATE_HOME \
        --uid "$NEWUID" \
        --home-dir "/home/$1" \
        --groups rtshplayers \
        --shell /bin/bash \
        "$1"

# set rtsh as password
echo "$1:rtsh" | chpasswd


# create basic layout of home directory
cd "/home/$1"
mkdir units/
mkdir buildings/

chown -R rtshsrv:rtshplayers units/
chown -R rtshsrv:rtshplayers buildings/

chmod 750 /units
chmod 750 /buildings

exit $?
