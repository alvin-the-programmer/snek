import sys

import urwid

import loop
from mainwidget import MainWidget
from header import Header
# from soundplayer.instance import player


palette = [
    ('reversed', 'standout', 'default'),
    ('b', 'bold', 'default')
]

main = MainWidget()

if len(sys.argv) == 2:
    path = sys.argv[1]
else:
    path = '.'

main.set_tracks(path)

top = urwid.Frame(main, header=urwid.LineBox(Header(path, main.set_tracks)))

loop.set(urwid.MainLoop(top, palette))
# loop.add_task(player.autoplay)
loop.run()
