#
# ~/.bash_profile
#

[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && exec startx

if [ -z "$DISPLAY" ]; then
	export LANG=en_US.UTF-8
	unset LANGUAGE
fi
