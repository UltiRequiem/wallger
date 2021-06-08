# Wallger: The Wallpaper Changer

<p>
<a href="https://github.com/UltiRequiem/wallger/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
<a href="https://github.com/UltiRequiem/wallger"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://github.com/UltiRequiem/wallger"><img alt="Code style: black" src="https://img.shields.io/tokei/lines/github.com/UltiRequiem/wallger?color=blue&label=Total%20Lines"></a>
<a href="https://pypi.org/project/wallger"><img alt="PyPI" src="https://img.shields.io/pypi/v/wallger"></a>
<a href="https://pepy.tech/project/wallger"><img alt="Downloads" src="https://pepy.tech/badge/wallger"></a>

</p>

<div align="center">
<a href="https://youtu.be/GtO8Rp69gHw">
<img src="https://user-images.githubusercontent.com/71897736/119916869-f67f4680-bf2a-11eb-9a52-7ab90169bf95.gif" width="5000"/>
</a>
</div>

<em>(To see a better quality version click on the gif)</em>

## Install Instructions

At the moment Wallger only supports Gnome, Mate and any Window Manager (i3wm, bspwm, dwm, etc).
If you are on a Window Manger you need to:

- Install `feh` (Adapt it to your distribution):

```bash
sudo pacman -S feh
```

If you are In Gnome or Mate you don't need to do that.

```bash
sudo pip install wallger
```

- Copy the example [config](./doc/config.json) in `~/.config/wm-wallpaper-changer/`

- Choose the Wallpaper provider you want and place the resolution of your monitor in the configuration file.
  You can investigate a little more about the parameters that the configuration receives in [docs](./doc).

Done! Now you can call `wallger` everywhere.
If you want to see some interesting use cases check [this](https://github.com/UltiRequiem/wallger/tree/master/doc).

If you have Python3.10 you may be wanna try this branch:
https://github.com/UltiRequiem/wallger/tree/python310
