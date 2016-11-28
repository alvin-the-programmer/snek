import urwid

import loop
import player
import resource
import misc


body_widget = None


def set_body(widget):
    global body_widget
    body_widget = widget


def set_tracks(w, path_widget):
    path = path_widget.edit_text
    sound_names = resource.load_sounds(path)
    track_window = get_track_window(sound_names)
    body_widget.contents[0] = (track_window, ('weight', 1))


def get_track_window(sound_names):
    column_labels = urwid.Columns([
        ('weight', 8, pad(urwid.Text(('b', u"Title"), wrap='clip'))),
        ('weight', 3, pad(urwid.Text(('b', u"Artist"), wrap='clip'))),
        ('weight', 5, pad(urwid.Text(('b', u"Album"), wrap='clip'))),
        ('weight', 3, pad(urwid.Text(('b', u"Duration"), wrap='clip'))),
    ], min_width=0)

    header = urwid.Pile([column_labels, urwid.Divider(u"-")])
    body_widget = get_track_list(sound_names)
    frame = urwid.Frame(body_widget, header=header)
    widget = urwid.LineBox(frame)
    return widget


def get_track_list(sound_names):
    player.set_queue(sound_names)   #
    track_data = resource.get_tracks_info(sound_names)

    tracks = []

    for num, t in enumerate(track_data):
        play_button = urwid.Button(u"\u25B6", on_press=player.play, user_data=num)

        title = urwid.Button(t['title'] or t['source_name'], on_press=player.play, user_data=num)
        title._label.wrap = 'clip'

        track = urwid.Columns([
            ('weight', 8, pad(title)),
            ('weight', 3, pad(urwid.Text(t['author'] or 'unknown', wrap='clip'))),
            ('weight', 5, pad(urwid.Text(t['album'] or 'unknown', wrap='clip'))),
            ('weight', 3, pad(urwid.Text(t['duration'], wrap='clip'))),
        ], min_width=0)

        attr_track = urwid.AttrMap(track, None, focus_map='reversed')
        tracks.append(attr_track)

    widget = urwid.ListBox(urwid.SimpleFocusListWalker(tracks))
    return widget


def pad(widget):
    widget = urwid.Padding(widget, left=1, right=1)
    return widget


def get_player_controls():
    info_widget= urwid.Columns([current_track_name(), current_track_time()])
    progress_widget = current_track_progress()
    media_widget = get_media_buttons()
    volume_widget = get_volume_buttons()
    divider = urwid.Divider(u"-")

    list_walker = urwid.SimpleFocusListWalker([
        info_widget,
        divider,
        progress_widget,
        divider,
        media_widget,
        volume_widget
    ])

    listBox = urwid.ListBox(list_walker)
    widget = urwid.LineBox(listBox)
    return widget


def get_volume_buttons():
    volTxt = urwid.Text(u"Volume: 10", align='center')

    def wrapper(widget, value):
        vol = player.volume(value)
        volTxt.set_text('Volume: ' + str(int(vol * 10)))

    volUp = urwid.Button(u"Vol \u25B2", on_press=wrapper, user_data=True)
    volDown = urwid.Button(u"Vol \u25BC", on_press=wrapper, user_data=False)

    volUp._label.align = 'center'
    volDown._label.align = 'center'

    volUp = misc.reverse_focus_color(volUp)
    volDown = misc.reverse_focus_color(volDown)

    widget = urwid.Columns([volTxt, volDown,volUp])
    return widget


def get_media_buttons():
    toggleb = urwid.Button(u"\u25B6 / \u275A\u275A", on_press=player.toggle)
    prevb = urwid.Button(u"\u25C0\u25C0", on_press=player.previous)
    nextb = urwid.Button(u"\u25B6\u25B6", on_press=player.next)

    toggleb._label.align = 'center'
    prevb._label.align = 'center'
    nextb._label.align = 'center'

    toggleb = misc.reverse_focus_color(toggleb)
    prevb = misc.reverse_focus_color(prevb)
    nextb = misc.reverse_focus_color(nextb)

    widget = urwid.Columns([prevb, toggleb, nextb])
    return widget


def current_track_name():
    widget = urwid.Text(u"", wrap='clip')

    def wrapper():
        name = player.current_track_name()
        widget.set_text(name)

    loop.add_task(wrapper)
    return widget


def current_track_progress():
    widget = urwid.ProgressBar(None, 'reversed')

    def wrapper():
        t = player.track_progress()
        widget.set_completion(t)

    loop.add_task(wrapper)
    return widget


def current_track_time():
    widget = urwid.Text(u"", align='right', wrap='clip')

    def wrapper():
        current, duration = player.track_time()
        current, duration = misc.format_time(current), misc.format_time(duration)
        formatted = u"{0} / {1}".format(current, duration)
        widget.set_text(formatted)

    loop.add_task(wrapper)
    return widget
