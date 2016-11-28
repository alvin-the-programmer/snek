import math

import urwid


def format_time(seconds):
    m, s = divmod(math.floor(seconds), 60)
    m, s = str(int(m)), str(int(s))
    time = '{0}:{1}'.format(m.zfill(2), s.zfill(2))
    return time


def reverse_focus_color(widget):
    return urwid.AttrMap(widget, None, focus_map='reversed')
