## TODO

## Configuration parameters

## Interesting uses
- New Wallpaper at startup
	If you use I3wm, you can put something like this in your i3config:
	```bash
exec ~/scripts/random_wallpaper
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
