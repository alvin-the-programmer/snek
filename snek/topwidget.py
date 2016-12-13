import urwid

from mainwidget import MainWidget
from header import Header


class TopWidget(urwid.Frame):
    def __init__(self, initial_path):
        body = MainWidget(initial_path)
        header = Header(initial_path, self.change_path)

        urwid.Frame.__init__(self, body, header=urwid.LineBox(header))


    def change_path(self, path):
        self.contents['body'][0].player.pause()

        new_body = MainWidget(path)
        self.contents['body'] = (new_body, None)
