main_loop = None
callbacks = []


def set(loop):
    global main_loop
    main_loop = loop


def add_task(cb):
    callbacks.append(cb)


def update(loop=None, user_data=None):
    for cb in callbacks:
        cb()

    main_loop.set_alarm_in(1, update)


def run():
    update()
    main_loop.run()
