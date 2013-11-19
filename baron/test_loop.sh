#!/bin/bash

while true; do clear; py.test; inotifywait -e modify *.py; done
