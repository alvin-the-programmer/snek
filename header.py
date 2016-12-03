import urwid

import body
import misc


header_widget = None


def get_path_header():
    global header_widget
    edit = misc.CustomEdit(u"Path: ", body.set_tracks)
    attr_edit = urwid.AttrMap(edit, None, focus_map='reversed')
    header_widget = edit
    return attr_edit


def set_path(path):
    edit= header_widget
    edit.set_edit_text(path)
    body.set_tracks(None, edit)
