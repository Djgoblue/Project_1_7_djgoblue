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
                print("\nInvalid choice. Type p to play or e to exit.")
        
        self.__setup()
        self.__shoe.set_cut_card()

        #While balance is greater than minimum bet keep playing
        playing = True
        while playing and self.__player.get_balance() >= 5:
            self.__play()
            if self.__player.get_balance() <5:
                print("\n You're broke. Come back with more money.")
                break          
            playing = self.__play_again
        
    #---------------------------------------------------------------

    #Setup

    def __welcome(self):
        print("\nWelcome to Python Blackjack!")
        print("\nI assume you already know how to play or else you shouldn't be gambling.")
        print("Beat the dealer to 21 without going over.")
        print("\nBlackjack pays 3:2 | Dealer stands on 17 | 8 decks in shoe | Choose where to cut shoe (Between 52 and 364)")
        print("Player starts with 100 chips | Minimum bet is 5")
        print("\nType p to play or e to exit.")
    
        
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
        if self.__player.get_hand_value() == 21:
            print("\nBlackjack!")
            self.__resolve(bet, player_blackjack=True)
            return
        
        #Player turn
        if self.__player_turn():
            self.__player.subtract_balance(bet)
            print(f"\n Bust! You lose ${bet}. Balance: ${self.__player.get_balance()}")
            return

        #Dealer turn
        self.__dealer.dealer_draw(self.__shoe)
        
        #Resolve round
        self.__resolve(bet)

    #---------------------------------------------------------------
    
    #Player turn
    def __player_turn(self):
        while True:
            print("\n Do you want to Hit or Stand?")
            print("Type h to hit or s to stand.")
            move = input().strip().lower()
            if move == "h":
                self.__player.draw(self.__shoe.draw())
                print(self.__player)
                if self.__player.is_bust():
                    return True
                if self.__player.get_hand_value() == 21:
                    print("Blackjack!")
                    return False
            elif move == "s":
                print(f"You stand at {self.__player.get_hand_value()}.")
                return False
            else:
                print("Type h to hit or s to stand.")
            
    #Betting stage
    def __collect_bet(self):
        while True:
            print(f"Place your bet. Balance: ${self.__player.get_balance()}")
            amount = input().strip()
            if not amount.isdigit():
                print("Please enter a whole number.")
                continue
            bet = int(amount)
            #Minimum bet is $5
            if bet < 5:
                print("Minimum bet is $5")
            elif bet > self.__player.get_balance():
                print("You don't have the money to bet that amount!")
            else:
                return bet
    
    #Resolution stage
    def __resolve(self, bet, player_blackjack=False):
        player_total = self.__player.get_hand_value()
        dealer_total = self.__dealer.get_hand_value()
        print(self.__player)
        print(self.__dealer)
        if player_blackjack:
            winnings = int(bet * 1.5)
            self.__player.add_balance(winnings)
            print(f"Blackjack! You win ${winnings}! Balance: ${self.__player.get_balance()}")
        elif self.__dealer.is_bust() or player_total > dealer_total:
            self.__player.add_balance(bet)
            print(f"You win ${bet}! Balance: ${self.__player.get_balance()}")
        elif player_total < dealer_total:
            self.__player.subtract_balance(bet)
            print(f"You lose ${bet}. Balance: ${self.__player.get_balance()}")
        elif player_total == dealer_total:
            print(f"Push! You and the dealer both have {player_total}. Balance: ${self.__player.get_balance()}")

    #Play again prompt
    def __play_again(self):
        while True:
            print("\nPlay again? Type y for yes and n for no.")
            choice = input().strip().lower()
            if choice == "y":
                return True
            elif choice == "n":
                return False
            else:
                print("\nType y for yes and n for no.")


#Run the game
if __name__ == "__main__":
    blackjack = Game()
    blackjack.run()