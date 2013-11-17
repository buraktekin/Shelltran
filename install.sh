#!/bin/bash
printf "\n
		 WELCOME TO SHELLTRAN
##########################################
# shelltran |	                         #
##########################################\n"
sudo mkdir /usr/local/shelltran
sudo cp ./shelltran.sh /usr/bin/shelltran
sudo cp ./shelltran.py /usr/local/shelltran/
sudo chmod 755 /usr/bin/shelltran /usr/local/shelltran/shelltran.py

printf "\nInstallation is completed.\n
Usage: shelltran <a word to search in dictionary>
Example: shelltran spider | OR | shelltran go through
\n"
exit
