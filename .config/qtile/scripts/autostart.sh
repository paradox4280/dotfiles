#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

#starting utility applications at boot time
dunst &
numlockx on &
run volumeicon &
run nm-applet &
unclutter -idle 10 &
picom --config $HOME/.config/picom/picom.conf &
feh --bg-fill $HOME/Downloads/wallhaven-l83o92.jpg

#flameshot &
#run pamac-tray &
#blueman-applet &
#/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# picom --config .config/picom/picom-blur.conf --experimental-backends &
#feh --randomize --bg-fill $HOME/Documents/wallpapers/*
#feh --bg-fill $HOME/Documents/wallpapers/wallhaven-9mjoy1.png

#starting user applications at boot time
#run discord &
#run telegram-desktop &
#nitrogen --random --set-zoom-fill &

#run atom &
#run thunar &
#run firefox &
#run dropbox &
#run spotify &
#run caffeine -a &
#run insync start &
#run vivaldi-stable &