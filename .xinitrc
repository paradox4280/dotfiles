#!/bin/sh

# while true; do
#     dwm > /dev/null 2>&1
# done

session=${1:-qtile}

case $session in
    dwm) exec dwm;;
    bspwm) exec bspwm;;
    i3|i3-wm) exec i3;;
    qtile) exec qtile start;;
esac
