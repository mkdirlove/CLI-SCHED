#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
from time import sleep

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		sleep(.01/10)

def main():
    os.system("clear")
    slowprint(bcolors.BOLD + bcolors.WARNING + "\n")
    os.system("toilet -f smbraille 'BSIT-WMAD SCHEDULE'")
    print("")
    slowprint(bcolors.BOLD + bcolors.GREEN + " [01] Monday Schedule")
    slowprint(bcolors.BOLD + bcolors.GREEN + " [02] Tuesday Schedule")
    slowprint(bcolors.BOLD + bcolors.GREEN + " [03] Wednesday Schedule")
    slowprint(bcolors.BOLD + bcolors.GREEN + " [04] Thursday Schedule")
    slowprint(bcolors.BOLD + bcolors.GREEN + " [05] Friday Schedule")
    slowprint(bcolors.BOLD + bcolors.GREEN + " [06] Personal Infos")
    slowprint(bcolors.BOLD + bcolors.GREEN + " [00] Close Schedule")
    slowprint(bcolors.BOLD + bcolors.WARNING + "\n")

    day = input(" ~> ")

    if day == '1' or day == '01':
        monday()
    elif day == '2' or day == '02':
        tuesday()
    elif day == '3' or day == '03':
        wednesday()
    elif day == '4' or day == '04':
        thursday()
    elif day == '5' or day == '05':
        friday()
    elif day == '6' or day == '06':
        about()
    elif day == '0' or day == '00':
        os.system("clear && exit")
    else:
        os.system("clear")
        print(" Invalid input!")

    
def about():
    os.system("clear")
    slowprint(bcolors.BOLD + bcolors.WARNING + "\n")
    os.system("toilet -f smbraille 'PERSONAL INFORMATION'")
    slowprint(bcolors.BOLD + bcolors.GREEN + "\n")
    slowprint(bcolors.BOLD + bcolors.GREEN + " STUDENT NO. :    0419-0932")
    slowprint(bcolors.BOLD + bcolors.GREEN + " NAME        :    John Arnold Catedrilla")
    slowprint(bcolors.BOLD + bcolors.GREEN + " COURSE      :    BSIT-WMAD")
    slowprint(bcolors.BOLD + bcolors.GREEN + " SECTION     :    BSIT-3A")
    slowprint(bcolors.BOLD + bcolors.GREEN + " YEAR        :    3rd Year")
    slowprint(bcolors.BOLD + bcolors.GREEN + " TYPE        :    Regular")
    slowprint(bcolors.BOLD + bcolors.GREEN + " GENDER      :    Male")
    slowprint(bcolors.BOLD + bcolors.WARNING + "\n")
    opt = input(" Back to main (y/n): ")

    if opt == 'y' or opt == 'Y':
        main()
    elif opt == 'n' or opt == 'N':
        os.system("clear && exit")
    else:
        os.system("clear")
        print(" Invalid input!")


def monday():
    os.system("clear")
    slowprint(bcolors.BOLD + bcolors.WARNING + "\n")
    os.system("toilet -f smbraille '            MONDAY SCHEDULE'")
    print("")
    slowprint(bcolors.BOLD + bcolors.GREEN + "\n ┌──────────────┬───────────────────────────┬──────┬───────────────────────┬────────────────┐")
    slowprint(" │ Subject Code │  Descriptive Title        │ Day  │         Time          │  Instructor    │")
    slowprint(" ├──────────────┼───────────────────────────┼──────┼───────────────────────┼────────────────┤")
    slowprint(" │ ITEP 308     │  System Integration       │ MON  │  07:30 AM - 10:30 AM  │  A. Cortez     │")
    slowprint(" ├──────────────┼───────────────────────────┼──────┼───────────────────────┼────────────────┤")
    slowprint(" │ ITEL 304     │  Integrative Programming  │ MON  │  12:00 PM - 03:00 PM  │  H. Natividad  │")
    slowprint(" ├──────────────┼───────────────────────────┼──────┼───────────────────────┼────────────────┤")
    slowprint(" │ ITEP 310     │  Social and Pro. Issues   │ MON  │  03:00 PM - 05:00 PM  │  M. Camba      │")
    slowprint(" └──────────────┴───────────────────────────┴──────┴───────────────────────┴────────────────┘")
    slowprint(bcolors.BOLD + bcolors.WARNING + "\n")
    opt = input(" Back to main (y/n): ")

    if opt == 'y' or opt == 'Y':
        main()
    elif opt == 'n' or opt == 'N':
        os.system("clear && exit")
    else:
        os.system("clear")
        print(" Invalid input!")


def tuesday():
    os.system("clear")
    slowprint(bcolors.BOLD + bcolors.WARNING + "\n")
    os.system("toilet -f smbraille '           TUESDAY SCHEDULE'") 
    print("")
    slowprint(bcolors.BOLD + bcolors.GREEN + "\n ┌──────────────┬───────────────────────────┬──────┬───────────────────────┬────────────────┐")
    slowprint(" │ Subject Code │  Descriptive Title        │ Day  │         Time          │  Instructor    │")
    slowprint(" ├──────────────┼───────────────────────────┼──────┼───────────────────────┼────────────────┤")
    slowprint(" │ ITEP 309     │  Networking 2             │ TUE  │  07:00 AM - 10:00 AM  │  H. Natividad  │")
    slowprint(" ├──────────────┼───────────────────────────┼──────┼───────────────────────┼────────────────┤")
    slowprint(" │ ITST 302     │  Client-Server Techs.     │ TUE  │  10:30 AM - 12:30 AM  │  A. Cortez     │")
    slowprint(" ├──────────────┼───────────────────────────┼──────┼───────────────────────┼────────────────┤")
    slowprint(" │ ITEP 308     │  System Integration       │ TUE  │  01:00 PM - 03:00 PM  │  A. Cortez     │")
    slowprint(" ├──────────────┼───────────────────────────┼──────┼───────────────────────┼────────────────┤")
    slowprint(" │ ITST 301     │  Principle of Web Design  │ TUE  │  03:00 PM - 05:00 PM  │  M. Camba      │")
    slowprint(" └──────────────┴───────────────────────────┴──────┴───────────────────────┴────────────────┘")
    slowprint(bcolors.BOLD + bcolors.WARNING + "\n")
    opt = input(" Back to main (y/n): ")

    if opt == 'y' or opt == 'Y':
        main()
    elif opt == 'n' or opt == 'N':
        os.system("clear && exit")
    else:
        os.system("clear")
        print(" Invalid input!")

    
def wednesday():
    os.system("clear")
    slowprint(bcolors.BOLD + bcolors.WARNING + "\n")
    os.system("toilet -f smbraille '           WEDNESDAY SCHEDULE'")
    print("")
    os.system("espeak 'today is your rest day so please get some rest'")
    opt = input(" Back to main (y/n): ")

    if opt == 'y' or opt == 'Y':
        main()
    elif opt == 'n' or opt == 'N':
        os.system("clear && exit")
    else:
        os.system("clear")
        print(" Invalid input!")
    
def thursday():
    os.system("clear")
    slowprint(bcolors.BOLD + bcolors.WARNING + "\n")
    os.system("toilet -f smbraille '          THURSDAY SCHEDULE'") 
    print("")
    slowprint(bcolors.BOLD + bcolors.GREEN + "\n ┌──────────────┬───────────────────────────┬──────┬───────────────────────┬────────────────┐")
    slowprint(" │ Subject Code │  Descriptive Title        │ Day  │         Time          │  Instructor    │")
    slowprint(" ├──────────────┼───────────────────────────┼──────┼───────────────────────┼────────────────┤")
    slowprint(" │ ITST 302     │  Client-Server Techs.     │ THU  │  07:70 AM - 10:30 AM  │  A. Cortez     │")
    slowprint(" ├──────────────┼───────────────────────────┼──────┼───────────────────────┼────────────────┤")
    slowprint(" │ ITEP 310     │  Social and Pro. Issues   │ THU  │  10:30 AM - 11:30 AM  │  M. Camba      │")
    slowprint(" ├──────────────┼───────────────────────────┼──────┼───────────────────────┼────────────────┤")
    slowprint(" │ ITEL 304     │  Integrative Programming  │ THU  │  01:00 PM - 03:00 PM  │  H. Natividad  │")
    slowprint(" ├──────────────┼───────────────────────────┼──────┼───────────────────────┼────────────────┤")
    slowprint(" │ ITEP 309     │  Networking 2             │ THU  │  03:00 PM - 05:00 PM  │  H. Natividad  │")
    slowprint(" └──────────────┴───────────────────────────┴──────┴───────────────────────┴────────────────┘")
    slowprint(bcolors.BOLD + bcolors.WARNING + "\n")
    opt = input(" Back to main (y/n): ")

    if opt == 'y' or opt == 'Y':
        main()
    elif opt == 'n' or opt == 'N':
        os.system("clear && exit")
    else:
        os.system("clear")
        print(" Invalid input!")


def friday():
    os.system("clear")
    slowprint(bcolors.BOLD + bcolors.WARNING + "\n")
    os.system("toilet -f smbraille '            FRIDAY SCHEDULE'") 
    print("")
    slowprint(bcolors.BOLD + bcolors.GREEN + "\n ┌──────────────┬───────────────────────────┬──────┬───────────────────────┬────────────────┐")
    slowprint(" │ Subject Code │  Descriptive Title        │ Day  │         Time          │  Instructor    │")
    slowprint(" ├──────────────┼───────────────────────────┼──────┼───────────────────────┼────────────────┤")
    slowprint(" │ ITST 301     │  Principle of Web Design  │ FRI  │  08:00 AM - 11:00 AM  │  M. Camba      │")
    slowprint(" └──────────────┴───────────────────────────┴──────┴───────────────────────┴────────────────┘")
    slowprint(bcolors.BOLD + bcolors.WARNING + "\n")
    opt = input(" Back to main (y/n): ")

    if opt == 'y' or opt == 'Y':
        main()
    elif opt == 'n' or opt == 'N':
        os.system("clear && exit")
    else:
        os.system("clear")
        print(" Invalid input!")


if __name__=="__main__":
    main()

