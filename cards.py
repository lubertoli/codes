import random
class Card:
    def __init__(self,rank,suit):
        # initializes the instance attributes of the object 
        self.rank = rank
        self.suit = suit
        
    def get_rank(self):
        # returns the rank of the card
        return self.rank
    
    def display(self):
        # matches the rank value to the rank name and displays the name of the card
        if self.rank == 1:
            self.rank = 'Ace'
        elif self.rank == 2:
            self.rank = 'Two'
        elif self.rank == 3:
            self.rank = 'Three'
        elif self.rank == 4:
            self.rank = 'Four'
        elif self.rank == 5:
            self.rank = 'Five'
        elif self.rank == 6:
            self.rank = 'Six'
        elif self.rank == 7:
            self.rank = 'Seven'
        elif self.rank == 8:
            self.rank = 'Eight'
        elif self.rank == 9:
            self.rank = 'Nine'
        elif self.rank == 10:
            self.rank = 'Ten'
        elif self.rank == 11:
            self.rank = 'Jack'
        elif self.rank == 12:
            self.rank = 'Queen'
        elif self.rank == 13:
            self.rank = 'King'
        print(str(self.rank) + ' of '+ self.suit)
                                                                                                                                        
class Deck:
    
    def __init__(self):
        #initializes the instance attributes of the object and creates the 52 cards in the deck
        self.ranks = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.deck = []
        for r in self.ranks:
            for s in self.suits:
                # creates the 52 cards in the deck  
                card = Card(r,s)
                self.deck.append(card)
       
    def shuffle(self):
        # shuffles the deck
        random.shuffle(self.deck)
    
    def deal(self):
        # removes the card at the top of the deck
        card_dealt = self.deck.pop(0)
        return card_dealt
    
class Player:
    
    def __init__(self):
        # initializes the instance attributes of the object and creates the player"s hand
        self.hand = []
    
    def add(self,card):
        # adds the card at the top of the deck to the player's hand
        self.hand.append(card)
    
    def ace_cards(self):
        # keeps count of the number of aces in the player's hand
        ace_count = 0
        for card in self.hand:
            rank = card.get_rank()        
            if rank == 'Ace':
                ace_count = ace_count + 1
        return ace_count
    
    def display(self):
        # displays the player's hand
        for card in self.hand:
            card.display()
            
def main():
    end_game = False
    while not end_game:
        #creates the deck
        deck = Deck()
        deck.shuffle()
        #creates the players
        player1 = Player()
        player2 = Player() 
        # deals 5 cards to player 1
        for t in range(1,6):
            card = deck.deal()
            player1.add(card)
        print('This is the hand of player 1:')
        player1.display()
        # deals 5 cards to player 2
        for t in range(1,6):
            card = deck.deal()
            player2.add(card)    
        print('This is the hand of player 2:')
        player2.display()
        #
        print("Number of ace cards in each player's hand:")
        player1_aces = player1.ace_cards()
        player2_aces = player2.ace_cards()
        print('Player 1 has ' + str(player1_aces) + ' aces')
        print('Player 2 has ' + str(player2_aces) + ' aces')
        # compares the number of aces in each player's hand
        if player1_aces == player2_aces:
            print('Result:')
            print('No winner, shuffle again')
            end_game = False        
        if player1_aces > player2_aces:
            print('Result:')
            print('Player 1 is the winner')
            end_game = True # ends the game 
        if player2_aces > player1_aces:
            print('Result:')
            print('Player 2 is the winner')
            end_game = True # ends the game       
main()    
        
    
                
    
                
                