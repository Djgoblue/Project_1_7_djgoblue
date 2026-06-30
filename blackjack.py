from player import Player
from deck import Shoe
from dealer import Dealer

class Game:
    def __init__(self):
        self.__dealer = Dealer()
    
    #Game Process
    def run(self):
        self.__welcome()
        self.__setup()

        #While balance is non-zero keep playing
        playing = True
        while playing and self.__balance() > 0:
            self.__play()

            if self.balance() <=0:
                print("\n You're broke. Come back with more money")
                break
            
            playing = self.__play_again
    #---------------------------------------------------------------