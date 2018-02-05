#!/usr/bin/env bash

chmod 222 /usr/local/luigi/datafiles/example3.txt

case "$1" in
    scheduler)
        luigid --background --logdir /usr/local/luigi/logs
        sudo crond -n
        ;;
    worker)
        sudo crond -n
        ;;
    *)
        echo "Received invalid command: ${1}"
        exit 1
        ;;
esac
