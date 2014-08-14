#!/bin/bash

while true
do
    clear
    if [ "$1" == "grammator" ]
    then
        py.test test_grammator* -x | tee /tmp/.baron_test_ouput
    else
        py.test -x | tee /tmp/.baron_test_ouput
    fi
    if ([ ! "$1" ] || [ "$1" == "grammator" ]) && [ "$(grep ': AssertionError' /tmp/.baron_test_ouput)" ]
    then
        grep "   def" /tmp/.baron_test_ouput | head -n 1 | sed 's/^ *//'
        sed 's/, *$//' /tmp/a > /tmp/aa
        sed 's/, *$//' /tmp/b > /tmp/bb
        colordiff -W $(stty size | cut -d " " -f 2) -y /tmp/aa /tmp/bb
        echo
        grep ":[0-9]\+:" /tmp/.baron_test_ouput | sed -n '$d;1p'
    elif [ "$1" == "dump" ] && [ "$(grep ': AssertionError' /tmp/.baron_test_ouput)" ] && [ ! "$(grep 'Warning: couldn.t write dumps output to debug file' /tmp/.baron_test_ouput)" ]
    then
        grep "   def" /tmp/.baron_test_ouput | head -n 1 | sed 's/^ *//'
        colordiff -W $(stty size | cut -d " " -f 2) -y /tmp/c /tmp/d
        echo
    fi
    inotifywait -e modify *.py ../baron/*.py
done
