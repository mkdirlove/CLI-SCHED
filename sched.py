#!/usr/bin/python3
#-*- coding: utf-8 -*-

# LIBRARIES
import os
import time

# FOREGROUND & BACKGROUND COLORS
#    black='\033[30m'
#    red='\033[31m'
#    green='\033[32m'
#    orange='\033[33m'
#    blue='\033[34m'
#    purple='\033[35m'
#    cyan='\033[36m'
#    lightgrey='\033[37m'
#    darkgrey='\033[90m'
#    lightred='\033[91m'
#    lightgreen='\033[92m'
#    yellow='\033[93m'
#    lightblue='\033[94m'
#    pink='\033[95m'
#    lightcyan='\033[96m'

def my_sched():
    os.system("clear")
    print("")
    print("\033[37m ┌──────────────┬──────────────────────────────────────┬──────┬─────────┬────────────┬──────┬─────────────────────┬──────┬────────────────┐  ┌────────────────────────┐")
    time.sleep(0.2)
    print("\033[37m │\033[33m Subject Code\033[37m │          \033[33mDescriptive title\033[37m           │ \033[33mUnit\033[37m │ \033[33mSection\033[37m │   \033[33mCourse\033[37m   │ \033[33mDay\033[37m  │        \033[33mTime\033[37m         │ \033[33mRoom\033[37m │   \033[33mInstructor\033[37m   │  │ MONDAY     -    \033[94mBLUE\033[37m   │")
    time.sleep(0.2)
    print("\033[37m ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤  ├────────────────────────┤")
    time.sleep(0.2)
    print("\033[37m │\033[91m    GEC 107   \033[37m│   \033[91mScience, Technology and Society    \033[37m│  \033[91m3   \033[37m│  \033[91mII-A   \033[37m│ \033[91mBSINFOTECH \033[37m│ \033[91mTUES \033[37m│ \033[91m01:00 PM - 04:00 PM \033[37m│ \033[91mTBA  \033[37m│ \033[91mA. Banasihan   \033[37m│  │ TUESDAY    -    \033[91mRED\033[37m    │")
    time.sleep(0.2)
    print("\033[37m ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤  ├────────────────────────┤")
    time.sleep(0.2)
    print("\033[37m │\033[94m   ITEC 204   \033[37m│   \033[94mData Structures and Algorithm      \033[37m│  \033[94m3   \033[37m│  \033[94mII-A   \033[37m│ \033[94mBSINFOTECH \033[37m│ \033[94mMOND \033[37m│ \033[94m07:30 AM - 09:30 AM \033[37m│ \033[94mTBA  \033[37m│ \033[94mM. Cardona     \033[37m│  │ WEDNESDAY  -    \033[33mORANGE\033[37m │")
    time.sleep(0.2)
    print("\033[37m ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤  ├────────────────────────┤")
    time.sleep(0.2)
    print("\033[37m │              │                                      │      │\033[33m  II-A   \033[37m│\033[33m BSINFOTECH \033[37m│\033[33m WEDN \033[37m│\033[33m 01:00 PM - 04:00 PM \033[37m│\033[33m TBA  \033[37m│\033[33m M. Cardona     \033[37m│  │ THURSDAY   -    WHITE  │")
    time.sleep(0.2)
    print("\033[37m ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤  ├────────────────────────┤")
    time.sleep(0.2)
    print("\033[37m │\033[94m   ITEC 205   \033[37m│\033[94m   Information Management             \033[37m│\033[94m  3   \033[37m│\033[94m  II-A   \033[37m│\033[94m BSINFOTECH \033[37m│\033[94m MOND \033[37m│\033[94m 09:30 AM - 11:30 AM \033[37m│\033[94m TBA  \033[37m│\033[94m R. Elomina     \033[37m│  │ FRIDAY     -    \033[93mYELLOW\033[37m │")
    time.sleep(0.2)
    print("\033[37m ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤  └────────────────────────┘")
    time.sleep(0.2)
    print("\033[37m │              │                                      │      │\033[93m  II-A   \033[37m│\033[93m BSINFOTECH \033[37m│\033[93m FRID \033[37m│\033[93m 08:00 AM - 11:00 AM \033[37m│\033[93m TBA  \033[37m│\033[93m R. Elomina     \033[37m│")
    time.sleep(0.2)
    print("\033[37m ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤")
    time.sleep(0.2)
    print("\033[37m │\033[94m   ITEL 201   \033[37m│\033[94m   Object-Oriented Programming        \033[37m│\033[94m  3   \033[37m│\033[94m  II-A   \033[37m│\033[94m BSINFOTECH \033[37m│\033[94m MOND \033[37m│\033[94m 03:00 PM - 05:00 PM \033[37m│\033[94m TBA  \033[37m│\033[94m G. Catedrilla  \033[37m│")
    time.sleep(0.2)
    print("\033[37m ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤")
    time.sleep(0.2)
    print("\033[37m │              │                                      │      │  II-A   │ BSINFOTECH │ THUR │ 01:00 PM - 04:00 PM │ TBA  │ G. Catedrilla  │")
    time.sleep(0.2)
    print("\033[37m ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤")
    time.sleep(0.2)
    print("\033[37m │\033[33m   ITEL 202   \033[37m│\033[33m   Platform Technologies              \033[37m│\033[33m  3   \033[37m│\033[33m  II-A   \033[37m│\033[33m BSINFOTECH \033[37m│\033[33m WEDN \033[37m│\033[33m 07:30 AM - 10:30 AM \033[37m│\033[33m TBA  \033[37m│\033[33m W. Suyat       \033[37m│")
    time.sleep(0.2)
    print("\033[37m ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤")
    time.sleep(0.2)
    print("\033[37m │              │                                      │      │  II-A   │ BSINFOTECH │ THUR │ 07:30 AM - 09:30 AM │ TBA  │ W. Suyat       │")
    time.sleep(0.2)
    print("\033[37m ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤")
    time.sleep(0.2)
    print("\033[37m │\033[94m   ITEP 203   \033[37m│\033[94m   Quantitative Metdhods              \033[37m│\033[94m  3   \033[37m│\033[94m  II-A   \033[37m│\033[94m BSINFOTECH \033[37m│\033[94m MOND \033[37m│\033[94m 01:00 PM - 03:00 PM \033[37m│\033[94m TBA  \033[37m│\033[94m J. Asor        \033[37m│")
    time.sleep(0.2)
    print("\033[37m ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤")
    time.sleep(0.2)
    print("\033[37m │              │                                      │      │\033[33m  II-A   \033[37m│\033[33m BSINFOTECH \033[37m│\033[33m WEDN \033[37m│\033[33m 04:00 PM - 05:00 PM \033[37m│\033[33m TBA  \033[37m│\033[33m J. Asor        \033[37m│")
    time.sleep(0.2)
    print("\033[37m ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤")
    time.sleep(0.2)
    print("\033[37m │\033[93m   PHED 213   \033[37m│\033[93m   Individual/Dual Sports Games       \033[37m│\033[93m  2   \033[37m│\033[93m  II-A   \033[37m│\033[93m BSINFOTECH \033[37m│\033[93m FRID \033[37m│\033[93m 03:00 PM - 05:00 PM \033[37m│\033[93m TBA  \033[37m│\033[93m P. Paruan      \033[37m│")
    time.sleep(0.2)
    print("\033[37m ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤")
    time.sleep(0.2)
    print("\033[37m │\033[91m  SOSLIT 103  \033[37m│\033[91m   Sosyedad at Literatura/Panitikan   \033[37m│\033[91m  3   \033[37m│\033[91m  II-A   \033[37m│\033[91m BSINFOTECH \033[37m│\033[91m TUES \033[37m│\033[91m 04:00 PM - 05:00 PM \033[37m│\033[91m TBA  \033[37m│\033[91m J. Lerios      \033[37m│")
    time.sleep(0.2)
    print("\033[37m ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤")
    time.sleep(0.2)
    print("\033[37m │              │                                      │      │  II-A   │ BSINFOTECH │ THUR │ 09:30 AM - 11:30 AM │ TBA  │ J. Lerios      │")
    time.sleep(0.2)
    print("\033[37m ├──────────────┴──────────────────────────────────────┴──────┴─────────┴────────────┴──────┴─────────────────────┴──────┴────────────────┤")
    time.sleep(0.2)
    print("\033[37m │                                          TOTAL UNITS : 23                                                                              │")
    time.sleep(0.2)
    print("\033[37m └────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘")

my_sched()
