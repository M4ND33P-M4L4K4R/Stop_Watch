#!/usr/bin/env python
import os
import time

print("\033[1m")
os.system("clear")

print("\033[31m-----------------------------")
n=int(input("\033[33m[\033[32m!\033[33m]\033[35m Set Timer : \033[32m"))
print("\033[31m-----------------------------")
time.sleep(2)
print("\033[33mYour ⏰  TiMe StArT NoW !!!!!!!!!")
time.sleep(2)
os.system("clear")

while n!=0:
    print("\033[1m")
    print("\033[32m----------------------------------")
    print(n,"\033[32mSecond Remaining...!")
    print("----------------------------------")
    time.sleep(1)
    os.system("figlet " + str(n)+"|lolcat")
    n=n-1
    time.sleep(1)
os.system("termux-tts-speak Your time is up")  
print("\033[1m\033[32m  ⏰⏰ Your Time Is Up ⏰⏰")
os.system("bash song.sh")
print()
print()


