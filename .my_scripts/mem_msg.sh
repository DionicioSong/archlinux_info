#!/bin/bash

mem_total=$(free -m | awk 'NR==2 {print $2}')
mem_used=$(free -m | awk 'NR==2 {print $3}')

mem_used_percent=$(printf "%.0f" $((mem_used*100/mem_total)))

echo  "$mem_used_percent%"
