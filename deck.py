import random

suits = ("Clubs", "Diamonds", "Hearts", "Spades")
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")

class Shoe:
    def __init__(self):
        self.__shoe = []
        self.__build()
    
    #Builds a new shoe of cards
    def __build(self):
        for _ in range(8):
            for suit in suits:
                for rank in ranks:
                    self.__shoe.append((rank, suit))
        random.shuffle(self.__shoe)