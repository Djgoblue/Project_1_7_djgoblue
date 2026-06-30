class Player:
    def __init__(self, name, balance = 100):
        self.__name = name
        self.__balance = balance
        self.__hand = []
    
    #Returns player's name
    def get_name(self):
        return self.__name

    #-------------------------------------
        
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
    
    #Decides which cards to reveal
    def show_hand(self, reveal_all = True):
        if reveal_all:
            return self.__hand
        else:
            #Dealer's first card is revealed, second card is hidden
            return [self.__hand[0], ("Hidden", "Card")]
    
    #Calculates the total value of the player's hand
    def get_hand_value(self):
        total = 0
        aces = 0
        for card in self.__hand:
            rank, suit = card
            if rank in ['Jack', 'Queen', 'King']:
                total += 10
            elif rank == 'Ace':
                total += 11
                aces += 1
            else:
                total += int(rank)
        
        #If total is over 21, change value of aces from 11 to 1
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
        return total
    
    #-------------------------------------
    
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

    #-------------------------------------

    #Defines over 21 as bust condition
    def is_bust(self):
        return self._get_hand_value() > 21
    
    #Show player's hand
    def __str__(self):
        ranks = ", ".join(self.show_hand())
        return f"{self.__name}'s hand: {ranks} | Value: {self.get_hand_value()}"