from player import Player


class CustomPlayer(Player):
    def play(self, widget, number):
        Player.play(self, number)


    def next(self, widget):
        Player.next(self)


    def toggle_shuffle(self, widget, state):
        Player.toggle_shuffle(self)


    def previous(self, widget):
        Player.previous(self)


    def toggle_play(self, widget):
        Player.toggle_play(self)
