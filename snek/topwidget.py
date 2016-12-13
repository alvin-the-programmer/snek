import urwid

from mainwidget import MainWidget
from header import Header
from loop import TaskLoop

class TopWidget(urwid.Frame):
    def __init__(self, main_loop, initial_path):
        self.task_loop = TaskLoop(main_loop)

        body = MainWidget(initial_path, self.task_loop)
        header = Header(initial_path, self.change_path)

        urwid.Frame.__init__(self, body, header=urwid.LineBox(header))


    def change_path(self, path):
        self.task_loop.stop()
        self.contents['body'][0].player.pause()

        new_body = MainWidget(path, self.task_loop)
        self.contents['body'] = (new_body, None)
