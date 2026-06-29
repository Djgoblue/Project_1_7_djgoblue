class Player:
    def __init__(self, name, balance = 100):
        self.name = name
        self.balance = balance
        self.hand = []
    
    #Hand methods

    #Add a card to the player's hand
    def draw(self, card):
        self.hand.append(card)
    
    #Clear the player's hand
    def clear(self):
        self.hand = []
    
    #Get player's hand
    def get_hand(self):
        return self.hand
    
    
    
    
