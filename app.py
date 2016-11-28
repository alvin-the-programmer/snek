import sys

import urwid

import loop
import resource
import player
import header
import body


palette = [
    ('reversed', 'standout', 'default'),
    ('b', 'bold', 'default')
]

pile = urwid.Pile([])
body.set_body(pile)
top = urwid.Frame(pile, header=header.get_path_header())

loop.set(urwid.MainLoop(top, palette))

pile.contents.append((body.get_track_window([]), ('weight', 1)))
pile.contents.append((body.get_player_controls(), ('given', 8)))

if len(sys.argv) == 2:
    path = sys.argv[1]
    header.set_path(path)

loop.add_task(player.autoplay)

loop.run()
