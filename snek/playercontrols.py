import urwid

import misc


class PlayerControls(urwid.ListBox):
    def __init__(self, player, task_loop):
        self.player = player
        self.task_loop = task_loop

        info_widget = urwid.Columns([self.current_track_name(), self.current_track_time()])
        progress_widget = self.current_track_progress()
        media_widget = self.get_media_buttons()
        volume_widget = self.get_volume_buttons()
        divider = urwid.Divider(u"-")

        list_walker = urwid.SimpleFocusListWalker([
            info_widget,
            divider,
            progress_widget,
            divider,
            media_widget,
            volume_widget
        ])

        urwid.ListBox.__init__(self, list_walker)


    def get_volume_buttons(self):
        volTxt = urwid.Text(u"Volume: 10", align='center')

        def wrapper(widget, value):
            vol = self.player.volume(value)
            volTxt.set_text('Volume: ' + str(int(vol * 10)))

        volUp = urwid.Button(u"Vol \u25B2", on_press=wrapper, user_data=True)
        volDown = urwid.Button(u"Vol \u25BC", on_press=wrapper, user_data=False)
        shuffleb = urwid.CheckBox(u"Shuffle", state=False, on_state_change=self.player.toggle_shuffle)

        volUp._label.align = 'center'
        volDown._label.align = 'center'
        shuffleb._label.align = 'center'


        volUp = misc.reverse_focus_color(volUp)
        volDown = misc.reverse_focus_color(volDown)
        shuffleb = misc.reverse_focus_color(shuffleb)

        widget = urwid.Columns([
            ('weight', 2, volTxt),
            ('weight', 2, volDown),
            ('weight', 2, volUp),
            ('weight', 12, shuffleb),
        ])
        return widget


    def get_media_buttons(self):
        toggleb = urwid.Button(u"\u25B6 / \u275A\u275A", on_press=self.player.toggle_play)
        prevb = urwid.Button(u"\u25C0\u25C0", on_press=self.player.previous)
        nextb = urwid.Button(u"\u25B6\u25B6", on_press=self.player.next)

        toggleb._label.align = 'center'
        prevb._label.align = 'center'
        nextb._label.align = 'center'

        toggleb = misc.reverse_focus_color(toggleb)
        prevb = misc.reverse_focus_color(prevb)
        nextb = misc.reverse_focus_color(nextb)

        widget = urwid.Columns([
            ('weight', 6, prevb),
            ('weight', 6, toggleb),
            ('weight', 6, nextb)
        ])
        return widget


    def current_track_name(self):
        widget = urwid.Text(u"", wrap='clip')

        def wrapper():
            name = self.player.current_track_name()
            widget.set_text(name)

        self.task_loop.add_task(wrapper)
        return widget


    def current_track_progress(self):
        widget = urwid.ProgressBar(None, 'reversed')

        def wrapper():
            t = self.player.track_progress()
            widget.set_completion(t)

        self.task_loop.add_task(wrapper)
        return widget


    def current_track_time(self):
        widget = urwid.Text(u"", align='right', wrap='clip')

        def wrapper():
            current, duration = self.player.track_time()
            current, duration = misc.format_time(current), misc.format_time(duration)
            formatted = u"{0} / {1}".format(current, duration)
            widget.set_text(formatted)

        self.task_loop.add_task(wrapper)
        return widget


def pad(widget):
    widget = urwid.Padding(widget, left=1, right=1)
    return widget
