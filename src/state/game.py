from enum import Enum


from component import Player, Dealer
from cards import Deck


class Game:
    def __init__(
        self,
        dealer: Dealer,
        player: Player,
        deck: Deck
    ):
        self.deck = deck
        self.dealer: Dealer = dealer
        self.player: Player = player
        self.round = 0

    def start(self):
        pass

    def next(self):
        pass

    def end(self):
        pass

    def new_deck(self):
        self.deck = Deck()

    def new_player(self):
        self.player = Player()
