from player import Player
from deck import Shoe


class Dealer(Player):
    def __init__(self):
        #Use .__init__ method of Player class on Dealer class
        super().__init__("Dealer")

    #Dealer methods
    
    def dealer_draw(self, shoe):
        #17 is the stand condition, keep drawing until condition is met
        while self.get_hand_value() < 17:
            new_card = shoe.draw()
            self.draw(new_card)
            rank, suit = new_card
            print(f"Dealer draws: {rank}")
            print(f"Dealer's total: {self.get_hand_value()}")
        #Dealer busts at over 21, otherwise dealer stands
        if self.is_bust():
            print("Dealer busts! You win!")
        else:
            print(f"Dealer stands at {self.get_hand_value()}")

    def partial_hand(self):
        #Dealer's first card is revealed, second card is hidden
        return self.show_hand(reveal_all=False)
    
    #Show dealer's hand
    def __str__(self):
        ranks = ", ".join(self.show_hand(reveal_all=True))
        return f"Dealer's hand: {ranks} | Value: {self.get_hand_value()}"
    