from player import Player
from deck import Shoe
from dealer import Dealer
import random as r

class Game:
    def __init__(self):
        self.__dealer = Dealer()
        self.__balance = 100
        self.__shoe = Shoe()

    #Game Process
    def run(self):
        self.__welcome()
        while True:
            choice = input().strip().lower()
            if choice == "p":
                break
            elif choice == "e":
                exit()
            else:
                print("\nInvalid choice. Type p to play or e to exit")
        
        self.__setup()
        self.__shoe.set_cut_card()

        # #While balance is non-zero keep playing
        # playing = True
        # while playing and self.__balance() > 0:
        #     self.__play()

        #     if self.__balance() <=0:
        #         print("\n You're broke. Come back with more money")
        #         break
            
        #     playing = self.__play_again
        
    #---------------------------------------------------------------

    #Setup

    def __welcome(self):
        print("\nWelcome to Python Blackjack!")
        print("\nI assume you already know how to play or else you shouldn't be gambling.")
        print("Beat the dealer to 21 without going over.")
        print("\nBlackjack pays 3:2 | Dealer stands on 17 | 8 decks in shoe | Choose where to cut shoe (Between 52 and 364)")
        print("Player starts with 100 chips | Minimum bet is 5")
        print("\nType p to play or e to exit")
    
        
    def __setup(self):
        print("\nWhat's your name?")
        name = input().strip()
        #Set name to player if nothing is entered
        if not name:
            name = "Player"
        self.__player = Player(name)
        print(f"\nWelcome, {self.__player.get_name()}!")
        print("Choose where to place the cut card. (Between 52 and 364)")

        

            
            

#Run the game
if __name__ == "__main__":
    blackjack = Game()
    blackjack.run()