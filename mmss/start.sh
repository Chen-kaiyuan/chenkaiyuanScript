#!/bin/bash

echo "start $3 with log from crate screen: $1 name: $2"
screen -dmS $2
screen -x -S $2 -p 0 -X stuff "tail -f catalina.out | grep '$3' >> $2.log"
screen -x -S $2 -p 0 -X stuff $'\n'
