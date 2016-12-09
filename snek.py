import sys

import urwid

import loop
import header
import body
import tracklist
import soundplayer.instance as player


palette = [
    ('reversed', 'standout', 'default'),
    ('b', 'bold', 'default')
]

pile = urwid.Pile([])
body.set_body(pile)
top = urwid.Frame(pile, header=header.get_header())

loop.set(urwid.MainLoop(top, palette))

pile.contents.append((tracklist.get_track_window([]), ('weight', 1)))
pile.contents.append((body.get_player_controls(), ('given', 8)))

if len(sys.argv) == 2:
    path = sys.argv[1]
    header.set_path(path)

loop.add_task(player.player.autoplay)

loop.run()
