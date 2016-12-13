import sys

import urwid

import loop
from topwidget import TopWidget


palette = [
    ('reversed', 'standout', 'default'),
    ('b', 'bold', 'default')
]


if len(sys.argv) == 2:
    path = sys.argv[1]
else:
    path = '.'

top = TopWidget(path)

loop.set(urwid.MainLoop(top, palette))
# loop.add_task(player.autoplay)
loop.run()
