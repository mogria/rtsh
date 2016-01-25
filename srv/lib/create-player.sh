#!/bin/bash


if [ -z "$1" ]; then
    echo "Usage: $0 [-n] playername"
    echo "pass the -n option if you don't want to create the users home directory"
    exit 1
fi

CREATE_HOME=1
CREATE_HOME_OPT="--create-home"
if [ "$1" == "-n" ]; then
    CREATE_HOME=0
    CREATE_HOME_OPT="-M"
    shift
fi

NEWUID=9001

# TODO: all users are created without a password. We need some way
# to register users. so this script can get these passwords.


while cut -d: -f3 "/etc/passwd" | grep -E "^$NEWUID$" > /dev/null; do
    NEWUID="$((NEWUID + 1))"
done

useradd --password "*" \
        $CREATE_HOME_OPT \
        --uid "$NEWUID" \
        --home-dir "/home/$1" \
        --groups rtshplayers \
        --shell /bin/bash \
        "$1"

useradd_exit="$?"

if [ "$useradd_exit" -eq 0 ]; then
    # set rtsh as password
    echo "$1:rtsh" | chpasswd

    if [ 1 -eq "$CREATE_HOME" ]; then
        # create basic layout of home directory
        cd "/home/$1"
        echo '{"class": "resources"}' > resources.json
        mkdir units/
        mkdir buildings/
        chown -R rtshsrv:$1 resources.json 
        chown -R rtshsrv:rtshplayers units/ buildings/

        chmod 750 resources.json units/ buildings/
        chmod -x resources.json
    fi
fi

# exit code is used by the python server
exit "$useradd_exit"
