class Player:
    def __init__(self, name, balance = 100):
        self.__name = name
        self.__balance = balance
        self.__hand = []
    
    #Hand methods

    #Add a card to the player's hand
    def draw(self, card):
        self.__hand.append(card)
    
    #Clear the player's hand
    def clear(self):
        self.__hand = []
    
    #Returns player's hand
    def get_hand(self):
        return self.__hand
    
    #Balance methods

    #Return player's balance
    def get_balance(self):
        return self.__balance
    
    #Add to player's balance
    def add_balance(self, amount):
        self.__balance += amount
    
    #Subtract from player's balance
    def subtract_balance(self, amount):
        self.__balance -= amount

    