import math
import random

import pyglet

# import soundloader.instance as sounds


class Player:
    def __init__(self, loader):
        self.loader = loader
        self.track_queue = loader.get_all_source_info()
        self.now_playing = pyglet.media.Player()
        self.track_queue = None
        self.track_num = None
        self.shuffle_order = None
        self.shuffle = False


    def set_queue(self, source_names):
        if self.now_playing.source:
            self.now_playing.pause()
            self.now_playing.next_source()

        self.track_queue = [self.loader.source_info(s) for s in source_names]


    def play(self, number):
        self.track_num = number

        if self.now_playing.source:
            self.now_playing.pause()
            self.now_playing.next_source()

        track = self.track_queue[number]
        source = self.loader.get_source(track['source_name'])
        self.now_playing.queue(source)
        self.now_playing.play()


    def next(self):
        if self.now_playing.source is None:
            return

        if self.shuffle:
            num = self.next_shuffle_num()
        else:
            num = self.next_inorder_num()

        self.play(None, num)


    def toggle_shuffle(self):
        if self.shuffle:
            self.shuffle = False
        else:
            self.shuffle = True
            self.shuffle_tracks()


    def next_inorder_num(self):
        num = self.track_num + 1

        if num == len(self.track_queue):
            num = 0

        return num


    def next_shuffle_num(self):
        current = self.shuffle_order.index(self.track_num)
        self.shuffle_num = current + 1

        if self.shuffle_num == len(self.shuffle_order):
            self.shuffle_num = 0

        num = self.shuffle_order[self.shuffle_num]
        return num


    def previous(self):
        if self.now_playing.source is None:
            return

        num = self.track_num - 1

        if num == -1:
            num = len(self.track_queue) - 1

        self.play(None, num)


    def toggle_play(self):
        if self.now_playing.playing:
            self.now_playing.pause()
        else:
            self.now_playing.play()


    def pause(self):
        if self.now_playing.playing:
            self.now_playing.pause()


    def volume(self, increase):
        if increase:
            new_volume = min(1, round(self.now_playing.volume + 0.1, 1))
        else:
            new_volume = max(0, round(self.now_playing.volume - 0.1, 1))

        self.now_playing.volume = new_volume
        return self.now_playing.volume


    def shuffle_tracks(self):
        self.shuffle_order = [i for i in range(0, len(self.track_queue))]
        random.shuffle(self.shuffle_order)


    def autoplay(self):
        if self.current_time() == self.track_duration():
            self.next(None)


    def track_progress(self):
        if self.now_playing.source is None:
            return 0
        percentage = (self.current_time() / self.track_duration()) * 100
        return math.floor(percentage)


    def current_track_name(self):
        if self.now_playing.source is None:
            return ''
        else:
            track = self.track_queue[self.track_num]
            author = track['author'] or 'unknown'
            title = track['title'] or track['source_name']
            name = '{} - {}'.format(author, title)
            return name


    def track_time(self):
        return self.current_time(), self.track_duration()


    def current_time(self):
        if self.now_playing.source is None:
            return 0
        else:
            return math.floor(self.now_playing.time)


    def track_duration(self):
        if self.now_playing.source is None:
            return 0
        else:
            return math.floor(self.now_playing.source.duration)
