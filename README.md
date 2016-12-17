# snek
A terminal based music player written in Python.

## Installing Dependencies
The easiest way to install snek's dependencies is through [pip](https://pypi.python.org/pypi/pip).

* Install [urwid](http://urwid.org/) console interface library
```
pip install urwid
```

* Install [pyglet](https://bitbucket.org/pyglet/pyglet/wiki/Home) multimedia library
```
pip install pyglet
```

* Install [AVbin](avbin.github.io/) audio decoding library (required for mp3 playback)

  * binary release available [here](http://avbin.github.io/AVbin/Download.html)

## Using snek
* Clone the repository
```
git clone https://github.com/azablan/snek.git
```
* cd into the directory and run snek.py, specifying a directory that contains audio files
```
python snek.py <absolute-path-to-music-directory>
```
## Screenshot

![Screenshot](https://cloud.githubusercontent.com/assets/14065730/21290374/c45b35dc-c485-11e6-88d1-340387bf15fb.png)
