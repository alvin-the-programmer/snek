import urwid

import misc


class Header(urwid.Columns):

    def __init__(self, on_path_change):
        quit = self.quit_button()
        edit = self.path_edit(on_path_change)

        widgets = [
            edit,
            quit
        ]

        urwid.Columns.__init__(self, widgets)


    def quit_button(self):
        def quit(w):
            raise urwid.ExitMainLoop()

        widget = urwid.Button(u"Quit", on_press=quit)
        widget._label.wrap = 'clip'
        widget._label.align = 'center'

        return widget


    def path_edit(self, enter_cb):
        edit = misc.CustomEdit(u"Path: ", enter_cb)
        widget = urwid.AttrMap(edit, None, focus_map='reversed')
        return widget
