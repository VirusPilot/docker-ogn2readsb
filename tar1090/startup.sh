#!/bin/bash

mkdir -p /run/tar1090

/usr/local/share/tar1090/tar1090.sh /run/tar1090 /tmp/readsb &

nginx -g "daemon off;"
