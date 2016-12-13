import sys

import urwid

import loop
from topwidget import TopWidget


palette = [
    ('reversed', 'standout', 'default'),
    ('b', 'bold', 'default')
]


main_loop = urwid.MainLoop(urwid.SolidFill('s'), palette)

if len(sys.argv) == 2:
    path = sys.argv[1]
else:
    path = '.'

top = TopWidget(main_loop, path)
main_loop.widget = top
main_loop.run()
