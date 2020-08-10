from random import shuffle
ranks=['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']
suits=['hearts', 'spades', 'diamonds', 'clubs']
values = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'jack':11, 'queen':12, 'king':13, 'ace':14}

class Cards():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank+" of " +self.suit

class Deck():
    def __init__(self):
        self.cards=[]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Cards(suit,rank))
    def shuffle(self):
        shuffle(self.cards)
    def get_one_card(self):
        return self.cards.pop()
    def __len__(self):
        return len(self.cards)

class Player():
    def __init__(self, name):
        self.name=name
        self.cards=[]
    def __str__(self):
        return f"Player {self.name} has {len(self.cards)} cards"
    def playCard(self):
        return self.cards.pop(0)
    def addCard(self, newCards):
        #Multiple card to add to the deck
        if type(newCards)==list:
            self.cards.extend(newCards)
        #One card to add to the deck
        else:
            self.cards.append(newCards)

deck=Deck()
deck.shuffle()
player1=Player("Firas")
player2=Player("Michael")
for i in range(0,26):
    player1.addCard(deck.get_one_card())
    player2.addCard(deck.get_one_card())    
gameon = True
war_cards=True
while gameon:
    if len(player1.cards)==0:
        print("Player one lost")
        gameon=False
        break
    if len(player2.cards)==0:
        print("Player two lost")
        gameon=False
        break
    player1_cards=[]
    player2_cards=[]
    player1_cards.append(player1.playCard())
    player2_cards.append(player2.playCard())
    while war_cards:
        if(player1_cards[-1].value<player2_cards[-1].value):
            player1.addCard(player1_cards)
            player1.addCard(player2_cards)
            war_cards=False
        elif player1_cards[-1].value>player2_cards[-1].value:
            player2.addCard(player2_cards)
            player2.addCard(player2_cards)
            war_cards=False
        else:
            print("War!")
            if(len(player1.cards)<2):
                print("Player one lost")
                gameon=False
                break
            elif(len(player2.cards)<2):
                print("Player two lost")
                gameon=False
                break
            else:
                for i in range(0,3):
                    player1_cards.append(player1.playCard())
                    player2_cards.append(player2.playCard())
