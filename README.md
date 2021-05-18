# The Wallpaper changer for Window Managers

<div align="center">
<a href="https://youtu.be/tNCVx82oKSQ">
<img src="https://user-images.githubusercontent.com/71897736/118586389-3fcbdb00-b760-11eb-93e8-ba29f97a31f4.gif" width="5000"/>
</a>
</div>

<em>(To see a better quality version click on the gif)</em>

## Install Instructions
- Clone the repository somewhere:
```bash
git clone https://github.com/ultirequiem/wmwc ~/Documents/wmwc
```
- Copy the example [config](./doc/config) in `~/.config/wm-wallpaper-changer`:
```bash
cp ~/Documents/wmwc/doc/config ~/.config/wm-wallpaper-changer/config
```
- Choose the Wallpaper provider you want and place the resolution of your monitor in the config.
You can investigate a little more about the parameters that the configuration receives in [docs](./doc).
- Set an alias:
```bash
echo alias wmwc='python3 ~/Documents/wmwc/main.py' > ~/.bashrc
```
Done! Now you can call `wmwc` everywhere.
If you want to see some interesting use cases check [this](./doc/README.md#interesting-uses).
