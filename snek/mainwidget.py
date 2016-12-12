import urwid

from soundloader.soundloader import Loader
from soundplayer.customplayer import CustomPlayer
from tracklist import TrackList
from playercontrols import PlayerControls


class MainWidget(urwid.Pile):
    def __init__(self):
        self.loader = Loader('.')
        self.player = CustomPlayer(self.loader)

        track_window = urwid.LineBox(TrackList(self.player, []))
        controls_window = urwid.LineBox(PlayerControls(self.player))

        widgets = [
            ('weight', 1, track_window),
            (8, controls_window)
        ]

        urwid.Pile.__init__(self, widgets)


    def set_tracks(self, path):
        self.loader = Loader(path)
        self.player = CustomPlayer(self.loader)

        sound_names = self.loader.sound_names
        track_data = self.loader.get_tracks_info(sound_names)
        track_window = urwid.LineBox(TrackList(self.player, track_data))
        controls_window = urwid.LineBox(PlayerControls(self.player))
        
        self.contents[0] = (track_window, ('weight', 1))
        self.contents[1] = (controls_window, ('given', 8))
