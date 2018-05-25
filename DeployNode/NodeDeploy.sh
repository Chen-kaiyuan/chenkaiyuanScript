#!/bin/bash

cd /root/
wget http://nodejs.org/dist/$1/node-$1-linux-x64.tar.gz
tar -zxvf node-$1-linux-x64.tar.gz
mv /root/node-$1-linux-x64 /opt/node
cat >> /etc/profile << EOF
export NODE_HOME=/opt/node/
export PATH=\$NODE_HOME/bin:\$PATH
EOF
echo 'Deploy node successful!'