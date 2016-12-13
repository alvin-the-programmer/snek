import urwid

from soundloader.soundloader import Loader
from soundplayer.customplayer import CustomPlayer
from tracklist import TrackList
from playercontrols import PlayerControls


class MainWidget(urwid.Pile):
    def __init__(self, path, task_loop):
        self.loader = Loader(path)
        self.player = CustomPlayer(self.loader)
        self.task_loop = task_loop

        track_data = self.loader.get_all_source_info()
        track_window = urwid.LineBox(TrackList(self.player, track_data))
        controls_window = urwid.LineBox(PlayerControls(self.player, self.task_loop))

        widgets = [
            ('weight', 1, track_window),
            (8, controls_window)
        ]

        urwid.Pile.__init__(self, widgets)
