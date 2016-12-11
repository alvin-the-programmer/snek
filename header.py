import urwid

import body
import misc


header_widget = None


def get_header():
    def quit(w):
        raise urwid.ExitMainLoop()

    quitb = urwid.Button(u"Quit", on_press=quit)
    quitb._label.wrap = 'clip'
    quitb._label.align = 'center'

    columns = urwid.Columns([
        ('weight', 8, get_path_header()),
        ('weight', 1, quitb)
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
    edit = header_widget
    edit.set_edit_text(path)
    body.set_tracks(None, edit)
