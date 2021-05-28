# The Wallpaper changer for Window Managers

<div align="center">
<a href="https://youtu.be/GtO8Rp69gHw">
<img src="https://user-images.githubusercontent.com/71897736/119916869-f67f4680-bf2a-11eb-9a52-7ab90169bf95.gif" width="5000"/>
</a>
</div>

<em>(To see a better quality version click on the gif)</em>

## Install Instructions
- Install `feh`:
```bash
sudo pacman -S feh
```
- Clone the repository somewhere:
```bash
git clone https://github.com/ultirequiem/wmwc ~/Documents/wmwc
```
- Install the requirements:
```bash
cd ~/Documents/wmwc ; pip3 install -r requirements.txt
```
- Copy the example [config](./doc/config) in `~/.config/wm-wallpaper-changer`:
```bash
cp ~/Documents/wmwc/doc/config.json ~/.config/wm-wallpaper-changer/config.json
```
- Choose the Wallpaper provider you want and place the resolution of your monitor in the configuration file.
You can investigate a little more about the parameters that the configuration receives in [docs](./doc).
- Set an alias:
```bash
echo alias wmwc='python3 ~/Documents/wmwc/main.py' >> ~/.bashrc
```
Done! Now you can call `wmwc` everywhere.
If you want to see some interesting use cases check [this](./doc/README.md#interesting-uses).
