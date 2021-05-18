## Docs
`[if_no_config](./if_no_config)` its used in case you don't set you personal config in `~/.config/wm-wallpaper-changer/config`

## Configuration parameters
- Monitor Section:
 - Long: Accept Number 
 - Height: Accept Number

- Wallpaper Section:
 - Provider: Accept one of the possible wallpaper providers.
 - Local: Accept a local directory path
 - Topic: Just for Wallhaven, accept a topic
 - NFSW: Accept false or true

- Misc Section:
 - Save: Accept true or false

## Interesting uses
- New Wallpaper at startup
	If you use I3wm, you can put something like this in your i3config:
	```bash
	exec python ~/Documents/wmwc/main.py
	```
	Similar if you use bspwm, put this in your bspwmrc:
	```bash
	python ~/Documents/wmwc/main.py
	```
- New Wallpaper at new terminal:
	Similar to above, put this on your .bashrc or .zshrc, etc:
	```bash
	python ~/Documents/wmwc/main.py
	```
