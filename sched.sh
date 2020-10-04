#!/bin/bash

# COLOR CODING
####################
# MOND = LIGHT BLUE
# TUES = RED
# WEDN = ORANGE
# THUR = WHITE
# FRID = YELLOW
####################

# TERMINAL COLORS
NO_COLOR="\e[0m"
WHITE="\e[0;17m"
BOLD_WHITE="\e[1;37m"
BLACK="\e[0;30m"
BLUE="\e[0;34m"
BOLD_BLUE="\e[1;34m"
GREEN="\e[0;32m"
BOLD_GREEN="\e[1;32m"
CYAN="\e[0;36m"
BOLD_CYAN="\e[1;36m"
RED="\e[0;31m"
BOLD_RED="\e[1;31m"
PURPLE="\e[0;35m"
BOLD_PURPLE="\e[1;35m"
BROWN="\e[0;33m"
BOLD_YELLOW="\e[1;33m"
GRAY="\e[0;37m"
BOLD_GRAY="\e[1;30m"
ORANGE="\e[0;49;33m"


clear
echo ""
sleep 0.1
echo -e "$BOLD_WHITE ┌──────────────┬──────────────────────────────────────┬──────┬─────────┬────────────┬──────┬─────────────────────┬──────┬────────────────┐$BOLD_WHITE  ┌────────────────────────┐"
sleep 0.1
echo -e "$BOLD_WHITE │$BOLD_GREEN Subject Code $BOLD_WHITE│$BOLD_GREEN          Descriptive title           $BOLD_WHITE│$BOLD_GREEN Unit $BOLD_WHITE│$BOLD_GREEN Section $BOLD_WHITE│$BOLD_GREEN   Course   $BOLD_WHITE│$BOLD_GREEN Day  $BOLD_WHITE│$BOLD_GREEN        Time         $BOLD_WHITE│$BOLD_GREEN Room $BOLD_WHITE│$BOLD_GREEN   Instructor   $BOLD_WHITE│$BOLD_WHITE  │ MONDAY     =$BOLD_BLUE    BLUE   $BOLD_WHITE│"
sleep 0.1
echo -e "$BOLD_WHITE ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤$BOLD_WHITE  ├────────────────────────┤"
sleep 0.1
echo -e "$BOLD_WHITE │$BOLD_RED    GEC 107   $BOLD_WHITE│$BOLD_RED   Science, Technology and Society    $BOLD_WHITE│$BOLD_RED  3   $BOLD_WHITE│$BOLD_RED  II-A   $BOLD_WHITE│$BOLD_RED BSINFOTECH $BOLD_WHITE│$BOLD_RED TUES $BOLD_WHITE│$BOLD_RED 01:00 PM - 04:00 PM $BOLD_WHITE│$BOLD_RED TBA  $BOLD_WHITE│$BOLD_RED A. Banasihan   $BOLD_WHITE│$BOLD_WHITE  │ TUESDAY    =$BOLD_RED    RED    $BOLD_WHITE│"
sleep 0.1
echo -e "$BOLD_WHITE ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤$BOLD_WHITE  ├────────────────────────┤"
sleep 0.1
echo -e "$BOLD_WHITE │$BOLD_BLUE   ITEC 204   $BOLD_WHITE│$BOLD_BLUE   Data Structures and Algorithm      $BOLD_WHITE│$BOLD_BLUE  3   $BOLD_WHITE│$BOLD_BLUE  II-A   $BOLD_WHITE│$BOLD_BLUE BSINFOTECH $BOLD_WHITE│$BOLD_BLUE MOND $BOLD_WHITE│$BOLD_BLUE 07:30 AM - 09:30 AM $BOLD_WHITE│$BOLD_BLUE TBA  $BOLD_WHITE│$BOLD_BLUE M. Cardona     $BOLD_WHITE│$BOLD_WHITE  │ WEDNESDAY  =$ORANGE    ORANGE $BOLD_WHITE│"
sleep 0.1
echo -e "$BOLD_WHITE ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤$BOLD_WHITE  ├────────────────────────┤"
sleep 0.1
echo -e "$BOLD_WHITE │              │                                      │      │$ORANGE  II-A   $BOLD_WHITE│$ORANGE BSINFOTECH $BOLD_WHITE│$ORANGE WEDN $BOLD_WHITE│$ORANGE 01:00 PM - 04:00 PM $BOLD_WHITE│$ORANGE TBA  $BOLD_WHITE│$ORANGE M. Cardona     $BOLD_WHITE│$BOLD_WHITE  │ THURSDAY   =$BOLD_WHITE    WHITE  │"
sleep 0.1
echo -e "$BOLD_WHITE ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤$BOLD_WHITE  ├────────────────────────┤"
sleep 0.1
echo -e "$BOLD_WHITE │$BOLD_BLUE   ITEC 205   $BOLD_WHITE│$BOLD_BLUE   Information Management             $BOLD_WHITE│$BOLD_BLUE  3   $BOLD_WHITE│$BOLD_BLUE  II-A   $BOLD_WHITE│$BOLD_BLUE BSINFOTECH $BOLD_WHITE│$BOLD_BLUE MOND $BOLD_WHITE│$BOLD_BLUE 09:30 AM - 11:30 AM $BOLD_WHITE│$BOLD_BLUE TBA  $BOLD_WHITE│$BOLD_BLUE R. Elomina     $BOLD_WHITE│$BOLD_WHITE  │ FRIDAY     =$BOLD_YELLOW    YELLOW $BOLD_WHITE│"
sleep 0.1
echo -e "$BOLD_WHITE ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤$BOLD_WHITE  └────────────────────────┘"
sleep 0.1
echo -e "$BOLD_WHITE │              │                                      │      │$BOLD_YELLOW  II-A   $BOLD_WHITE│$BOLD_YELLOW BSINFOTECH $BOLD_WHITE│$BOLD_YELLOW FRID $BOLD_WHITE│$BOLD_YELLOW 08:00 AM - 11:00 AM $BOLD_WHITE│$BOLD_YELLOW TBA  $BOLD_WHITE│$BOLD_YELLOW R. Elomina     $BOLD_WHITE│$BOLD_WHITE"
sleep 0.1
echo -e "$BOLD_WHITE ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤$BOLD_WHITE"
sleep 0.1
echo -e "$BOLD_WHITE │$BOLD_BLUE   ITEL 201   $BOLD_WHITE│$BOLD_BLUE   Object-Oriented Programming        $BOLD_WHITE│$BOLD_BLUE  3   $BOLD_WHITE│$BOLD_BLUE  II-A   $BOLD_WHITE│$BOLD_BLUE BSINFOTECH $BOLD_WHITE│$BOLD_BLUE MOND $BOLD_WHITE│$BOLD_BLUE 03:00 PM - 05:00 PM $BOLD_WHITE│$BOLD_BLUE TBA  $BOLD_WHITE│$BOLD_BLUE G. Catedrilla  $BOLD_WHITE│$BOLD_WHITE"
sleep 0.1
echo -e "$BOLD_WHITE ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤$BOLD_WHITE"
sleep 0.1
echo -e "$BOLD_WHITE │              │                                      │      │  II-A   │ BSINFOTECH │ THUR │ 01:00 PM - 04:00 PM │ TBA  │ G. Catedrilla  │$BOLD_WHITE"
sleep 0.1
echo -e "$BOLD_WHITE ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤$BOLD_WHITE"
sleep 0.1
echo -e "$BOLD_WHITE │$ORANGE   ITEL 202   $BOLD_WHITE│$ORANGE   Platform Technologies              $BOLD_WHITE│$ORANGE  3   $BOLD_WHITE│$ORANGE  II-A   $BOLD_WHITE│$ORANGE BSINFOTECH $BOLD_WHITE│$ORANGE WEDN $BOLD_WHITE│$ORANGE 07:30 AM - 10:30 AM $BOLD_WHITE│$ORANGE TBA  $BOLD_WHITE│$ORANGE W. Suyat       $BOLD_WHITE│$BOLD_WHITE"
sleep 0.1
echo -e "$BOLD_WHITE ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤$BOLD_WHITE"
sleep 0.1
echo -e "$BOLD_WHITE │              │                                      │      │  II-A   │ BSINFOTECH │ THUR │ 07:30 AM - 09:30 AM │ TBA  │ W. Suyat       │$BOLD_WHITE"
sleep 0.1
echo -e "$BOLD_WHITE ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤$BOLD_WHITE"
sleep 0.1
echo -e "$BOLD_WHITE │$BOLD_BLUE   ITEP 203   $BOLD_WHITE│$BOLD_BLUE   Quantitative Metdhods              $BOLD_WHITE│$BOLD_BLUE  3   $BOLD_WHITE│$BOLD_BLUE  II-A   $BOLD_WHITE│$BOLD_BLUE BSINFOTECH $BOLD_WHITE│$BOLD_BLUE MOND $BOLD_WHITE│$BOLD_BLUE 01:00 PM - 03:00 PM $BOLD_WHITE│$BOLD_BLUE TBA  $BOLD_WHITE│$BOLD_BLUE J. Asor        $BOLD_WHITE│$BOLD_WHITE"
sleep 0.1
echo -e "$BOLD_WHITE ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤$BOLD_WHITE"
sleep 0.1
echo -e "$BOLD_WHITE │              │                                      │      │$ORANGE  II-A   $BOLD_WHITE│$ORANGE BSINFOTECH $BOLD_WHITE│$ORANGE WEDN $BOLD_WHITE│$ORANGE 04:00 PM - 05:00 PM $BOLD_WHITE│$ORANGE TBA  $BOLD_WHITE│$ORANGE J. Asor        $BOLD_WHITE│$BOLD_WHITE"
sleep 0.1
echo -e "$BOLD_WHITE ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤$BOLD_WHITE"
sleep 0.1
echo -e "$BOLD_WHITE │$BOLD_YELLOW   PHED 213   $BOLD_WHITE│$BOLD_YELLOW   Individual/Dual Sports Games       $BOLD_WHITE│$BOLD_YELLOW  2   $BOLD_WHITE│$BOLD_YELLOW  II-A   $BOLD_WHITE│$BOLD_YELLOW BSINFOTECH $BOLD_WHITE│$BOLD_YELLOW FRID $BOLD_WHITE│$BOLD_YELLOW 03:00 PM - 05:00 PM $BOLD_WHITE│$BOLD_YELLOW TBA  $BOLD_WHITE│$BOLD_YELLOW P. Paruan      $BOLD_WHITE│$BOLD_WHITE"
sleep 0.1
echo -e "$BOLD_WHITE ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤$BOLD_WHITE"
sleep 0.1
echo -e "$BOLD_WHITE │$BOLD_RED  SOSLIT 103  $BOLD_WHITE│$BOLD_RED   Sosyedad at Literatura/Panitikan   $BOLD_WHITE│$BOLD_RED  3   $BOLD_WHITE│$BOLD_RED  II-A   $BOLD_WHITE│$BOLD_RED BSINFOTECH $BOLD_WHITE│$BOLD_RED TUES $BOLD_WHITE│$BOLD_RED 04:00 PM - 05:00 PM $BOLD_WHITE│$BOLD_RED TBA  $BOLD_WHITE│$BOLD_RED J. Lerios      $BOLD_WHITE│$BOLD_WHITE"
sleep 0.1
echo -e "$BOLD_WHITE ├──────────────┼──────────────────────────────────────┼──────┼─────────┼────────────┼──────┼─────────────────────┼──────┼────────────────┤$BOLD_WHITE"
sleep 0.1
echo -e "$BOLD_WHITE │              │                                      │      │  II-A   │ BSINFOTECH │ THUR │ 09:30 AM - 11:30 AM │ TBA  │ J. Lerios      │$BOLD_WHITE"
sleep 0.1
echo -e "$BOLD_WHITE ├──────────────┴──────────────────────────────────────┴──────┴─────────┴────────────┴──────┴─────────────────────┴──────┴────────────────┤$BOLD_WHITE"
sleep 0.1
echo -e "$BOLD_WHITE │                                          TOTAL UNITS : 23                                                                              │$BOLD_WHITE"
sleep 0.1
echo -e "$BOLD_WHITE └────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘$BOLD_WHITE"
echo ""
