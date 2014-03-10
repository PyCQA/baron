#!/bin/bash

while true
do
    clear
    py.test -x | tee /tmp/.baron_test_ouput
    if [ ! "$1" ] && [ "$(grep ': AssertionError' /tmp/.baron_test_ouput)" ]
    then
        grep "   def" /tmp/.baron_test_ouput | head -n 1 | sed 's/^ *//'
        sed 's/, *$//' /tmp/a > /tmp/aa
        sed 's/, *$//' /tmp/b > /tmp/bb
        colordiff -W $(stty size | cut -d " " -f 2) -y /tmp/aa /tmp/bb
    elif [ "$1" == "dump" ] && [ "$(grep ': AssertionError' /tmp/.baron_test_ouput)" ]
    then
        grep "   def" /tmp/.baron_test_ouput | head -n 1 | sed 's/^ *//'
        colordiff -W $(stty size | cut -d " " -f 2) -y /tmp/c /tmp/d
        echo
    fi
    inotifywait -e modify *.py
done
