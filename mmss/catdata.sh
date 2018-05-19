#!/bin/bash

echo "start $3 with log from crate screen: $1 name: $2"
cat catalina.out | grep '$3' >> $2.log

