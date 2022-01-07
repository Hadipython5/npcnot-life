#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os,sys,time
def clear():
    os.system("clear")
def kata(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./300)
def baner():
    time.sleep(0.1)
    kata("""\n\t\033[90m~  ~  ~\033[92m┌∩┐\033[94m(\033[91m◣_◢\033[94m)\033[92m┌∩┐\033[90m~  ~  ~
\t\033[92m     BY:samsul hadi
\t\033[90m -----------------------\033[94m\n
===========================================\033[00m
Program \033[1;91m: \033[1;96mAI chatbot\033[00m
version \033[1;91m: \033[1;96m1.10.100\033[00m
password\033[1;92m: \033[1;95mheksakosioiheksekontaheksafobia
language\033[1;91m: \033[4;92mPython\033[00m
\033[94m===========================================\033[00m""")
def balik():
    f=input("\033[00m\t[\033[96mEnter to active program\033[00m]")
    if f == "":
       os.system("python npc.py")
    else:
       sys.exit("\033[1;91mexit\033[00m")
    time.sleep(0.1)
    print("\n\033[90mpassword salah!! \033[1;93m")
if __name__=="__main__":
     clear()
     baner()
     balik()
