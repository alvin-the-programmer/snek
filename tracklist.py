import urwid

import soundloader.instance as sounds
from playerinstance import player_instance as player


track_data = None
track_window = None


def get_track_window(sound_names):
    frame = urwid.Frame(None, header=get_column_header())
    set_track_window(frame)

    set_track_data(sound_names)
    update(None, 'album')

    widget = urwid.LineBox(frame)
    return widget


def set_track_data(sound_names):
    global track_data
    track_data = sounds.loader.get_tracks_info(sound_names)


def set_track_window(widget):
    global track_window
    track_window = widget


def update(w, sort_key):
    body = (get_track_list(sort_key), None)
    track_window.contents['body'] = body


def get_track_list(sort_key):
    track_d = sort_tracks(track_data, sort_key)
    player.set_queue([t['source_name']for t in track_d])
    tracks = []

    for num, t in enumerate(track_d):
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


def sort_tracks(tracks, sort_data):
    sorted_tracks = sorted(tracks, key=lambda track:track[sort_data])
    return sorted_tracks


def get_column_header():
    title = urwid.Button(
        ('b', u"Title"),
        on_press=update, user_data='title'
    )
    artist = urwid.Button(
        ('b', u"Artist"),
        on_press=update, user_data='author'
    )
    album = urwid.Button(
        ('b', u"Album"),
        on_press=update, user_data='album'
    )
    duration = urwid.Button(
        ('b', u"Duration"),
        on_press=update, user_data='duration'
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


def pad(widget):
    widget = urwid.Padding(widget, left=1, right=1)
    return widget
