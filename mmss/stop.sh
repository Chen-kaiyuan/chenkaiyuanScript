#!/bin/bash

echo "stop $3 with log from crate screen: $1 name: $2"
ps -x | grep "tail -f catalina.out" | awk '{print $1}' | xargs kill -9
screen -x -S $2 -p 0 -X stuff "exit"
screen -x -S $2 -p 0 -X stuff $'\n'

