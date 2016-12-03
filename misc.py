import math

import urwid


class CustomEdit(urwid.Edit):
    def __init__(self, caption, cb):
        urwid.Edit.__init__(self, caption)
        self.on_enter = cb

    def keypress(self, size, key):
        if key == 'enter':
            self.on_enter(self, self)
        urwid.Edit.keypress(self, size, key)


def format_time(seconds):
    m, s = divmod(math.floor(seconds), 60)
    m, s = str(int(m)), str(int(s))
    time = '{0}:{1}'.format(m.zfill(2), s.zfill(2))
    return time


def reverse_focus_color(widget):
    return urwid.AttrMap(widget, None, focus_map='reversed')
