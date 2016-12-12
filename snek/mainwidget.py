import urwid

import soundloader.instance as loader
import soundplayer.instance as p
from tracklist import TrackList
from body import PlayerControls
import body


class MainWidget(urwid.Pile):
    def __init__(self):
        track_window = urwid.LineBox(TrackList([]))
        controls_window = urwid.LineBox(PlayerControls(p.player))

        widgets = [
            ('weight', 1, track_window),
            (8, controls_window)
        ]

        urwid.Pile.__init__(self, widgets)


    def set_tracks(self, path):
        loader.set_path(path)
        sound_names = loader.loader.sound_names
        track_window = urwid.LineBox(TrackList(sound_names))
        self.contents[0] = (track_window, ('weight', 1))
