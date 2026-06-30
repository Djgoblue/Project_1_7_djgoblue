import random

suits = ("Clubs", "Diamonds", "Hearts", "Spades")
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")

class Shoe:
    def __init__(self):
        self.__shoe = []
        self.__build()
    
    #Builds a new shoe of cards
    def build(self):
        for _ in range(8):
            for suit in suits:
                for rank in ranks:
                    self.__shoe.append((rank, suit))
        random.shuffle(self.__shoe)
    
    #Draw card
    def draw(self):
        return self.__shoe.pop
    
    #Set cut card
    def set_cut_card(self, depth):
        if depth < 52 or depth > 416:
            raise ValueError("Cut card depth must be between 52 and 416")
        self.__cut_card_depth = depth
        
    #Determine if cut card has been reached
    def cut_card_reached(self):
        return len(self.__shoe) <= self.__cut_card_depth