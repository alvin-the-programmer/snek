import urwid

import body
import misc


header_widget = None


def get_header():
    def wrapper(w):
        raise urwid.ExitMainLoop()
    quit = urwid.Button(u"Quit", on_press=wrapper)
    quit._label.wrap = 'clip'
    quit._label.align = 'center'

    columns = urwid.Columns([
        ('weight', 8, get_path_header()),
        ('weight', 1, quit)
    ])
    widget = urwid.LineBox(columns)
    return widget


def get_path_header():
    global header_widget
    edit = misc.CustomEdit(u"Path: ", body.set_tracks)
    widget = urwid.AttrMap(edit, None, focus_map='reversed')
    header_widget = edit
    return widget


def set_path(path):
    edit= header_widget
    edit.set_edit_text(path)
    body.set_tracks(None, edit)
