# Wallger: The Wallpaper Changer

![CodeQL](https://github.com/UltiRequiem/wallger/workflows/CodeQL/badge.svg)
![CI](https://github.com/UltiRequiem/wallger/workflows/CI/badge.svg)
[![Code Style](https://img.shields.io/badge/Code%20Style-Black-000000.svg)](https://github.com/psf/black)
[![PyPi Version](https://img.shields.io/pypi/v/wallger)](https://pypi.org/project/wallger)
![Repo Size](https://img.shields.io/github/repo-size/ultirequiem/wallger?style=flat-square&label=Repo)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![Lines of Code](https://img.shields.io/tokei/lines/github.com/UltiRequiem/wallger?color=blue&label=Total%20Lines)

https://user-images.githubusercontent.com/71897736/129631224-d4f00320-265c-4514-9086-a01b26cfdfd2.mp4

## Install

From [PyPI](https://pypi.org/project/wallger)

```bash
pip install wallger
```

From [GitHub](https://github.com/UltiRequiem/wallger)

```bash
pip install git+https:/github.com/UltiRequiem/wallger
```

You may need to install this with administrative permissions, depending on your
configuration.

## Example Config

> `~/.config/wallger/config.json`:

```json
{
  "resolution": [1600, 900],
  "provider": "wallhaven",
  "path": "/home/zero/disk/sabare/wallger",
  "topic": "anime",
  "tool": "feh",
  "nsfw": false
}
```

- Resolution: The resolution of you monitor

  > The expected value is a tuple of two integers, eg. [2800, 1900]

- Provider: The wallpapers provider site

  > Currently just "Wallhaven" or "Unsplash"

- Path: Where to save the images

> So you can see your previous wallpapers later

- Topic: The topic of your wallpaper

> Not all providers support this, eg. "Math", "Mirai Nikki", "JavaScript"

- Tool: The tool to change the Wallpaper

> Accepts one of these 👉 ["feh", "gnome", "mate", "kde"]

- NSFW: Not safe for work

**There are not default values, config is required!**

## Alternatives

- [@neosaile/wpupd](https://github.com/NeoSaile/wpupd): Very similar to this, written in
  Node.js, by me and my father 😆

### License

Wallger is licensed under the [MIT License](./license).
