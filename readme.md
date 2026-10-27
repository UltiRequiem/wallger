# Wallger: The Wallpaper Changer

[![PyPi Version](https://img.shields.io/pypi/v/wallger)](https://pypi.org/project/wallger)

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

- Resolution: The resolution of your monitor

  > The expected value is an array of two integers, eg. [2800, 1900]

- Provider: The wallpaper provider

  > Currently, only "Wallhaven" or "Unsplash"

- Path: Where to save the images

> So you can see your previous wallpapers later

- Topic: The topic of your wallpaper

> Not all providers support this, eg. "Math", "Mirai Nikki", "JavaScript"

- Tool: The CLI tool used to change the wallpaper

> Accepts one of these 👉 ["feh", "gnome", "mate", "kde"]

- NSFW: Not safe for work

**There are not default values, config is required!**

### License

Wallger is licensed under the [MIT License](./license).
