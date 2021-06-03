# Wallger: The Wallpaper Changer

<div align="center">
<a href="https://youtu.be/GtO8Rp69gHw">
<img src="https://user-images.githubusercontent.com/71897736/119916869-f67f4680-bf2a-11eb-9a52-7ab90169bf95.gif" width="5000"/>
</a>
</div>

<em>(To see a better quality version click on the gif)</em>

## Install Instructions

At the moment Walger only supports Gnome, Mate and any Window Manager(i3wm, bspwm, etc).
If you are on a Window Manger you need to:

- Install `feh` (Adapt it to your distribution):

```bash
sudo pacman -S feh
```

If you are In Gnome or Mate you don't need to do that.

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

Done! Now you can call `wallger` everywhere.
If you want to see some interesting use cases check [this](https://github.com/UltiRequiem/wallger/tree/master/doc).
