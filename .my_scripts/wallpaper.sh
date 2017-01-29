#!/bin/bash

shopt -s nullglob
cd ~/Pictures/Wallpapers

while true; do
    sleep 35m

    files=()
    for i in *.jpg *.png; do
	[[ -f $i  ]] && files+=("$i")
    done
    range=${#files[@]}

    ((range)) && feh --bg-scale "${files[RANDOM % range]}"
done
