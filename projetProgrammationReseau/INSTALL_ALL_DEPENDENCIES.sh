#!/bin/bash

sudo apt-get update
sudo apt-get install mysql-server

wget https://github.com/iredmail/iRedMail/archive/1.5.2.tar.gz
tar -xf 1.5.5.tar.gz
chmod +x /home/ado/Documents/Network_Programming/Script_shell/iRedMail-1.5.2/iRedmail.sh
./iRedMail-1.5.2/iRedmail.sh