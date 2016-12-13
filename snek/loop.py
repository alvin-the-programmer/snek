import urwid


class TaskLoop:
    def __init__(self, main_loop):
        self.tasks = []
        self.main_loop = main_loop
        self.handle = None
        self.run_tasks()


    def add_task(self, cb):
        self.tasks.append(cb)


    def run_tasks(self, loop=None, user_data=None):
        for cb in self.tasks:
            cb()

        self.handle = self.main_loop.set_alarm_in(1, self.run_tasks)


    def stop(self):
        if self.handle is not None:
            print 'stop'
            self.main_loop.remove_alarm(self.handle)
