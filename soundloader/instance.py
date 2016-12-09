from soundloader import SoundLoader

loader = SoundLoader('.')

def set(path):
    global loader
    loader = SoundLoader(path)
