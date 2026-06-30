import random as r

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
        r.shuffle(self.__shoe)
    
    #Draw card
    def draw(self):
        return self.__shoe.pop
    
    #Set cut card
    def set_cut_card(self):
        while True:
            cut = input().strip()
            if cut == "":
                self.__cut_card_depth = r.randint(52, 364)
                break
            if not cut.isdigit():
                print("\nPlease enter a whole number.")
                continue
            cut = int(cut)
            if cut < 52 or cut > 364:
                print("\nCut card depth must be between 52 and 364")
                continue
            self.__cut_card_depth = cut
            break
        
    #Determine if cut card has been reached
    def cut_card_reached(self):
        return len(self.__shoe) <= self.__cut_card_depth