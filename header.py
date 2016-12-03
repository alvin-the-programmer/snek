import urwid

import body
import misc

header_widget = None


def get_path_header():
    edit = misc.CustomEdit(u"Path: ", body.set_tracks)
    widget = urwid.Columns([edit])
    global header_widget
    header_widget = widget
    return widget


def set_path(path):
    edit, options = header_widget.contents[0]
    edit.set_edit_text(path)
    body.set_tracks(None, edit)
