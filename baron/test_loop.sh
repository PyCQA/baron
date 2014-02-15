#!/bin/bash

while true
do
    clear
    py.test
    if [ "$?" == "1" ]
    then
        sed 's/, *$//' /tmp/a > /tmp/aa
        sed 's/, *$//' /tmp/b > /tmp/bb
        colordiff -W $(stty size | cut -d " " -f 2) -y /tmp/aa /tmp/bb
    else
        echo "ok"
    fi
    inotifywait -e modify *.py
done
