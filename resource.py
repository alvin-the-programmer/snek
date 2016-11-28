import os

import pyglet

import body
import misc


SOUND_EXTS = ('.mp3', '.wav')


loader = pyglet.resource.Loader([])


def get_source(name):
    source = loader.media(name)
    return source


def get_tracks_info(track_names):
    tracks_info = [source_info(t) for t in track_names]
    return tracks_info


def source_info(source_name):
    source = get_source(source_name)

    info = {
        'source_name' : source_name,
        'title' : source.info.title,
        'author' : source.info.author,
        'album' : source.info.album,
        'duration' : misc.format_time(source.duration)
    }

    return info


def source_title(name):
    source = get_source(name)
    return source.info.title or name


def load_sounds(path):
    sound_names = []
    resource_paths = []

    for root, dirs, files in os.walk(path):
        sounds = [f for f in files if f.endswith(SOUND_EXTS)]

        if sounds:
            resource_paths.append(root)
            sound_names.extend(sounds)

    global loader
    loader = pyglet.resource.Loader(resource_paths)

    return sound_names
