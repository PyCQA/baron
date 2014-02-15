#!/bin/bash

while true
do
    clear
    py.test
    if [ "$?" == "1" ]
    then
        colordiff -W $(stty size | cut -d " " -f 2) -y /tmp/a /tmp/b
    fi
    inotifywait -e modify *.py
done
