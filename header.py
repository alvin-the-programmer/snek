import urwid

import body


header_widget = None


def get_path_header():
    edit = urwid.Edit(caption=u"Path: ")
    enter = urwid.Button(u"enter", on_press=body.set_tracks, user_data=edit)
    widget = urwid.Columns([edit, enter])
    global header_widget
    header_widget = widget
    return widget


def set_path(path):
    edit, options = header_widget.contents[0]
    edit.set_edit_text(path)
    body.set_tracks(None, edit)
