from player import Player
from deck import Shoe


class Dealer(Player):
    def __init__(self):
        #Use .__init__ method of Player class on Dealer class
        super().__init__("Dealer")

