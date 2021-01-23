#!/bin/bash
apt install pv -y
clear
echo -e "      \033[31mRequirements is Going to be Satisfied " | pv -qL 10
apt update -y
apt upgrade -y 
apt install ruby -y
gem install lolcat
apt install termux-api -y
apt install mpv -y
pip install os
pkg install python -y 
pkg install python2
echo

echo
echo  "     setup Successfully   "
sleep 3
chmod +x song.sh
chmod +x Stop_watch.py
python Stop_watch.py
