#!/usr/bin/env bash

#From server

adduser web #creates a new user on the server
chown web:users /home/web #gives the user ownership of the web directory

apt-get install sudo #install sudo

visudo #edit file to add sudo privelages to the web user

#log off and ssh to the server using the web user ssh web@....

#update server
sudo apt-get update
sudo apt-get upgrade

#install some tools for MariaDB
sudo apt-get install python-software-properties
sudo apt-get install software-properties-common

#add repo (works for Debian 9.6)
sudo apt-get install software-properties-common dirmngr
sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xF1656F24C74CD1D8
sudo add-apt-repository 'deb [arch=amd64,i386,ppc64el] https://mirrors.evowise.com/mariadb/repo/10.3/debian stretch main'

#update system
sudo apt-get update

#install server and client
sudo apt-get install mariadb-server mariadb-client
nano /etc/mysql/my.cnf #change bind address to 0.0.0.0

service mysql restart #restart mysql

#connecting python to maria
sudo apt-get install libmariadbclient-dev libssl-dev python-mysqldb
wget http://ftp.kaist.ac.kr/mysql/Downloads/Connector-Python/mysql-connector-python_2.1.8-1debian9_all.deb
dpkg -i mysql-connector-python_2.1.8-1debian9_all.deb

# flask setup
mkdir source
cd source

sudo apt-get install curl
curl -O http://peak.telecommunity.com/dist/ez_setup.py # install ez_setup
sudo python ez_setup.py
sudo easy_install pip
sudo pip install flask
