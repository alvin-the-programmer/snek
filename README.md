# snek
A terminal based music player written in Python.

## Installing Dependencies
1. install [urwid](http://urwid.org/) console interface library
```
pip install urwid
```

2. install [pyglet](www.pyglet.org/) multimedia library
```
pip install pyglet
```

3. install [AVbin](avbin.github.io/) audio decoding library (required for mp3 playback)

  * binary release available [here](http://avbin.github.io/AVbin/Download.html)

## Using snek
1. clone the repository
```
git clone https://github.com/azablan/snek.git
```
2. cd into the directory and run snek.py, specifying a directory that contains audio files
```
python snek.py <absolute-path-to-music-directory>
```
