from soundloader import Loader


loader = Loader('.')


def set_path(path):
    global loader
    loader = Loader(path)
