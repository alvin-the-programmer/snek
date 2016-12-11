import urwid

import soundloader.instance as loader
from soundplayer.instance import player


class TrackList(urwid.Frame):
    def __init__(self, sound_names):
        self.track_data = loader.loader.get_tracks_info(sound_names)

        header = self.get_column_header()
        body = self.get_track_list('album')
        urwid.Frame.__init__(self, body, header=header)


    def get_track_list(self, sort_key):
        track_data = self.sort_tracks(sort_key)
        player.set_queue([t['source_name']for t in track_data])
        tracks = []

        for num, t in enumerate(track_data):
            title = urwid.Button(
                t['title'] or t['source_name'],
                on_press=player.play, user_data=num
            )
            author = urwid.Button(
                t['author'] or 'unknown',
                on_press=player.play, user_data=num
            )
            album = urwid.Button(
                t['album'] or 'unknown',
                on_press=player.play, user_data=num
            )
            duration = urwid.Button(
                t['duration'],
                on_press=player.play, user_data=num
            )

            title._label.wrap = 'clip'
            author._label.wrap = 'clip'
            album._label.wrap = 'clip'
            duration._label.wrap = 'clip'

            track = urwid.Columns([
                ('weight', 8, pad(title)),
                ('weight', 3, pad(author)),
                ('weight', 5, pad(album)),
                ('weight', 3, pad(duration))
            ], min_width=0)

            attr_track = urwid.AttrMap(track, None, focus_map='reversed')
            tracks.append(attr_track)

        widget = urwid.ListBox(urwid.SimpleFocusListWalker(tracks))
        return widget


    def get_column_header(self):
        title = urwid.Button(
            ('b', u"Title"),
            on_press=self.update, user_data='title'
        )
        artist = urwid.Button(
            ('b', u"Artist"),
            on_press=self.update, user_data='author'
        )
        album = urwid.Button(
            ('b', u"Album"),
            on_press=self.update, user_data='album'
        )
        duration = urwid.Button(
            ('b', u"Duration"),
            on_press=self.update, user_data='duration'
        )

        title._label.wrap = 'clip'
        artist._label.wrap = 'clip'
        album._label.wrap = 'clip'
        duration._label.wrap = 'clip'

        header = urwid.Columns([
            ('weight', 8, pad(title)),
            ('weight', 3, pad(artist)),
            ('weight', 5, pad(album)),
            ('weight', 3, pad(duration))
        ], min_width=0)

        widget = urwid.Pile([header, urwid.Divider(u"-")])
        return widget


    def sort_tracks(self, sort_key):
        sorted_tracks = sorted(self.track_data, key=lambda track:track[sort_key])
        return sorted_tracks


    def update(self, widget, sort_key):
        body = (self.get_track_list(sort_key), None)
        self.contents['body'] = body


def pad(widget):
    widget = urwid.Padding(widget, left=1, right=1)
    return widget
