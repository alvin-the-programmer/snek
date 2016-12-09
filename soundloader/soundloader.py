import os
import math

import pyglet


class SoundLoader:
    SOUND_EXTS = ('.mp3', '.wav')


    def __init__(self, path):
        resource_paths = self.get_resource_paths(path)
        self.loader = pyglet.resource.Loader(resource_paths)
        self.sound_names = self.get_sound_names(path)
        self.path = path


    def get_resource_paths(self, root):
        resource_paths = []

        for root, dirs, files in os.walk(root):
            resource_paths.append(root)

        return resource_paths


    def get_sound_names(self, root):
        sound_names = []

        for root, dirs, files in os.walk(root):
            sounds = [f for f in files if f.endswith(self.SOUND_EXTS)]

            if sounds:
                sound_names.extend(sounds)

        return sound_names


    def get_source(self, source_name):
        source = self.loader.media(source_name)
        return source


    def get_tracks_info(self, source_names):
        tracks_info = [self.source_info(s) for s in source_names]
        return tracks_info


    def source_info(self, source_name):
        source = self.get_source(source_name)

        info = {
            'source_name' : source_name,
            'title' : source.info.title,
            'author' : source.info.author,
            'album' : source.info.album,
            'duration' : self.format_time(source.duration)
        }

        return info


    def source_title(self, source_name):
        source = self.get_source(source_name)
        return source.info.title or name

    def format_time(self, seconds):
        m, s = divmod(math.floor(seconds), 60)
        m, s = str(int(m)), str(int(s))
        time = '{0}:{1}'.format(m.zfill(2), s.zfill(2))
        return time
