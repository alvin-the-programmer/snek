import math
import random

import pyglet

import resource


now_playing = pyglet.media.Player()
track_queue = None
track_num = None
shuffle = False
shuffle_order = None


def set_queue(source_names):
    if now_playing.source:
        now_playing.pause()
        now_playing.next_source()

    global track_queue
    track_queue = [resource.source_info(s) for s in source_names]


def play(w, number):
    global track_num
    track_num = number

    if now_playing.source:
        now_playing.pause()
        now_playing.next_source()

    track = track_queue[number]
    source = resource.get_source(track['source_name'])
    now_playing.queue(source)
    now_playing.play()


def next(w):
    if now_playing.source is None:
        return

    if shuffle:
        num = next_shuffle_num()
    else:
        num = next_inorder_num()

    play(None, num)


def toggle_shuffle(w):
    global shuffle

    if shuffle:
        shuffle = False
        w.set_label(u"Shuffle: Off")
    else:
        shuffle = True
        shuffle_tracks()
        w.set_label(u"Shuffle: On")


def next_inorder_num():
    num = track_num + 1

    if num == len(track_queue):
        num = 0

    return num


def next_shuffle_num():
    current = shuffle_order.index(track_num)
    shuffle_num = current + 1

    if shuffle_num == len(shuffle_order):
        shuffle_num = 0

    num = shuffle_order[shuffle_num]
    return num


def previous(w):
    if now_playing.source is None:
        return

    num = track_num - 1

    if num == -1:
        num = len(track_queue) - 1

    play(None, num)


def toggle_play(w):
    if now_playing.playing:
        now_playing.pause()
    else:
        now_playing.play()


def volume(increase):
    if increase:
        new_volume = min(1, round(now_playing.volume + 0.1, 1))
    else:
        new_volume = max(0, round(now_playing.volume - 0.1, 1))

    now_playing.volume = new_volume
    return now_playing.volume


def shuffle_tracks():
    global shuffle_order
    shuffle_order = [i for i in range(0, len(track_queue))]
    random.shuffle(shuffle_order)


def autoplay():
    if current_time() == track_duration():
        next(None)


def track_progress():
    if now_playing.source is None:
        return 0
    percentage = (current_time() / track_duration()) * 100
    return math.floor(percentage)


def current_track_name():
    if now_playing.source is None:
        return ''
    else:
        track = track_queue[track_num]
        author = track['author'] or 'unknown'
        title = track['title'] or track['source_name']
        name = '{} - {}'.format(author, title)
        return name


def track_time():
    return current_time(), track_duration()


def current_time():
    if now_playing.source is None:
        return 0
    else:
        return math.floor(now_playing.time)


def track_duration():
    if now_playing.source is None:
        return 0
    else:
        return math.floor(now_playing.source.duration)
