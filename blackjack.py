from player import Player
from deck import Shoe
from dealer import Dealer
import random as r

class Game:
    def __init__(self):
        self.__dealer = Dealer()
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

        #While balance is greater than minimum bet keep playing
        playing = True
        while playing and self.__player.get_balance() >= 5:
            self.__play()
            if self.__player.get_balance() <5:
                print("\n You're broke. Come back with more money")
                break          
            # playing = self.__play_again
        
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

    #---------------------------------------------------------------    

    #Play round

    def __play(self):
        print(f" Your chips: {self.__player.get_balance()}")

        #Shuffle if cut card reached
        if self.__shoecut_card_reached():
            print("\n Cut card reached - reshuffling...")
            self.__shoe = Shoe()
            self.__shoe.set_cut_card()
    
        #Betting stage
        bet = self.__collect_bet()

        #Deal intial two cards
        self.__player.clear()
        self.__dealer.clear()
        for _ in range(2):
            self.__player.draw
            for _ in range(2):
                self.__player.draw(self.__shoe.draw())
                self.__dealer.draw(self.__shoe.draw())

        #Show initial hands
        print(f"Player shows: {self.__player}")
        dealer_hand = self.__dealer.show_hand(reveal_all=False)
        print(f"Player shows: {dealer_hand[0]} | {dealer_hand[1]}")

        #Check for player blackjack
        if self.__player.get_hand_value() ==21:
            print("\nBlackjack!")
            self.__resolve(bet, player_blackjack=True)
            return
        
            

#Run the game
if __name__ == "__main__":
    blackjack = Game()
    blackjack.run()