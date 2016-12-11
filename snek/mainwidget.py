import urwid

import soundloader.instance as loader
import tracklist
import body


class MainWidget(urwid.Pile):
    def __init__(self):
        track_window = tracklist.get_track_window([])
        player_controls = body.get_player_controls()

        widgets = [
            ('weight', 1, track_window),
            (8, player_controls)
        ]

        urwid.Pile.__init__(self, widgets)


    def set_tracks(self, path):
        loader.set_path(path)
        sound_names = loader.loader.sound_names
        track_window = tracklist.get_track_window(sound_names)
        self.contents[0] = (track_window, ('weight', 1))
