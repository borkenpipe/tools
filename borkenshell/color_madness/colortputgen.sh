#!/usr/bin/env bash

# Unicode symbols
readonly PS_SYMBOL_DARWIN=''
readonly PS_SYMBOL_LINUX='$'
readonly PS_SYMBOL_OTHER='%'
readonly GIT_BRANCH_SYMBOL='⑂ '
readonly GIT_BRANCH_CHANGED_SYMBOL='+'
readonly GIT_NEED_PUSH_SYMBOL='⇡'
readonly GIT_NEED_PULL_SYMBOL='⇣'

# Solarized colorscheme
readonly FG_BASE03="\[$(tput setaf 8)\]"
readonly FG_BASE02="\[$(tput setaf 0)\]"
readonly FG_BASE01="\[$(tput setaf 10)\]"
readonly FG_BASE00="\[$(tput setaf 11)\]"
readonly FG_BASE0="\[$(tput setaf 12)\]"
readonly FG_BASE1="\[$(tput setaf 14)\]"
readonly FG_BASE2="\[$(tput setaf 7)\]"
readonly FG_BASE3="\[$(tput setaf 15)\]"

readonly BG_BASE03="\[$(tput setab 8)\]"
readonly BG_BASE02="\[$(tput setab 0)\]"
readonly BG_BASE01="\[$(tput setab 10)\]"
readonly BG_BASE00="\[$(tput setab 11)\]"
readonly BG_BASE0="\[$(tput setab 12)\]"
readonly BG_BASE1="\[$(tput setab 14)\]"
readonly BG_BASE2="\[$(tput setab 7)\]"
readonly BG_BASE3="\[$(tput setab 15)\]"

readonly FG_YELLOW="\[$(tput setaf 3)\]"
readonly FG_ORANGE="\[$(tput setaf 9)\]"
readonly FG_RED="\[$(tput setaf 1)\]"
readonly FG_MAGENTA="\[$(tput setaf 5)\]"
readonly FG_VIOLET="\[$(tput setaf 13)\]"
readonly FG_BLUE="\[$(tput setaf 4)\]"
readonly FG_CYAN="\[$(tput setaf 6)\]"
readonly FG_GREEN="\[$(tput setaf 2)\]"

readonly BG_YELLOW="$(tput setab 3)"
readonly BG_ORANGE="\[$(tput setab 9)\]"
readonly BG_RED="\[$(tput setab 1)\]"
readonly BG_MAGENTA="\[$(tput setab 5)\]"
readonly BG_VIOLET="\[$(tput setab 13)\]"
readonly BG_BLUE="\[$(tput setab 4)\]"
readonly BG_CYAN="\[$(tput setab 6)\]"
readonly BG_GREEN="\[$(tput setab 2)\]"

readonly DIM="\[$(tput dim)\]"
readonly REVERSE="\[$(tput rev)\]"
readonly RESET="$(tput sgr0)"
readonly BOLD="\[$(tput bold)\]"

for i in $(seq 1 150) ; do
    printf "$(tput setab $i) \"\\[\$(tput setab $i)\\]\"  $RESET\n"
done
