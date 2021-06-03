# Wallger: The Wallpaper Changer
<p>
<a href="https://github.com/UltiRequiem/wallger/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
<a href="https://github.com/UltiRequiem/wallger"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://github.com/UltiRequiem/wallger"><img alt="Code style: black" src="https://img.shields.io/tokei/lines/github.com/UltiRequiem/wallger?color=blue&label=Total%20Lines"></a>
</p>

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
git clone https://github.com/ultirequiem/wallger ~/Documents/wallger
```

- Install the requirements:

```bash
cd ~/Documents/wallger ; pip3 install -r requirements.txt
```

- Copy the example [config](./doc/config.json) in `~/.config/wm-wallpaper-changer/`:

```bash
cp ~/Documents/wallger/doc/config.json ~/.config/wallger/config.json
```

- Choose the Wallpaper provider you want and place the resolution of your monitor in the configuration file.
  You can investigate a little more about the parameters that the configuration receives in [docs](./doc).
- Set an alias:

```bash
echo alias wallger='python3 ~/Documents/wallger/main.py' >> ~/.bashrc
```

Done! Now you can call `wallger` everywhere.
If you want to see some interesting use cases check [this](https://github.com/UltiRequiem/wallger/tree/master/doc).

If you have Python3.10 you may be wanna try this branch:
https://github.com/UltiRequiem/wallger/tree/python310
