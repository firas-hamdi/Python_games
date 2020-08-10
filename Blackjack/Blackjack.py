from random import shuffle
suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Ace', 'Queen', 'King', 'Jack']
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Ace':[1, 11], 'Queen':10, 'King':10, 'Jack':10}
class Card():
    '''
    Class presenting a card
    ...
    ATTRIBUTES:
    -----------
    rank: str
        The rank of the card
        @ref ranks
    suit: str
        The suit of the card
        @ref suits
    value: int
        The value of the card
        @ref values
    -----------
    Methods:
    -----------
    __str__()
        Prints the rank of the card and its suit
    '''
    def __init__(self, rank, suit):
        '''
        Parameters:
        -----------
        rank: str
            The rank of the card
            @ref ranks
        suit: str
            The suit of the card
            @ref suits
        value: int
            The value of the card
            @ref values
        '''
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
    def __str__(self):
        '''
        Prints the card's rank and suit
        '''
        return f"{self.rank} of {self.suit}"

class Deck():
    '''
    Class presenting a deck containing 52 cards
    ...
    ATTRIBUTES:
    -----------
    cards: list
        list of card objects
    -----------
    Methods:
    -----------
    __len__()
        Prints the number of cards in a deck
    shuffle_deck()
        Shuffles the deck
    get_one_card()
        Takes one card from the deck randomly
    '''
    def __init__(self):
        '''
        Creates a deck of 52 card objects
        '''
        self.cards = []
        for rank in ranks:
            for suit in suits:
                card = Card(rank, suit)
                self.cards.append(card)
    def __len__(self):
        '''
        returns the length of the deck
        '''
        return len(self.cards)
    def shuffle_deck(self):
        '''
        Shuffles the deck 
        '''
        shuffle(self.cards)
    def get_one_card(self):
        '''
        Takes one card from the deck randomly
        '''
        return self.cards.pop()

class Player():
    '''
    Parameters:
    -----------
    name: str
        The name of the player
    chips: int
        The chips a player has
    -----------
    Methods:
    -----------
    __str__()
        Prints the name of the player and the number of his chips
    bet()
        Asks the player to make his bet
    win_bet()
        Add the chips won after a bet
    lose_bet()
        Reduce the chips lost after a bet
    continue_playing():
        Asks the player about continuing the game or not
    '''
    def __init__(self, name, chips):
        '''
        Parameters:
        -----------
        name: str
            The name of the player
        chips: int
            The chips that the player has
        '''
        self.name = name
        self.chips = chips
    def __str__(self):
        '''
        Prints the player's name and the chips owned
        '''
        return f"{self.name} have {self.chips} chips"
    def bet(self):
        '''
        Returns the bet made by the player
        '''
        while True:
            try:
                bet = int(input("How many chips you want to bet?: "))
                if bet > self.chips:
                    print("You do not have enough chips to bet")
                    continue
            except TypeError:
                print("Please input a number")
                continue
            else:
                print(f"{self.name} have made a bet of {bet}")
                break
        return bet 
    def win_bet(self, bet):
        '''
        Add chips to the player after winning a bet
        '''
        self.chips += bet
        return self.chips
    def lose_bet(self, bet):
        '''
        Remove chips from the player after losing a bet
        '''
        self.chips -= bet
        return self.chips
    def continue_playing(self):
        '''
        Asks the player to continue playing or not
        '''
        accepted_values = ['Y', 'N']
        continue_game = ''
        while continue_game.upper() not in accepted_values:
            continue_game = input("You want to continue playing, Y or N? ")
            if continue_game.upper() not in accepted_values:
                print("This is a yes or no question please, Y or N")
        if continue_game.upper() == 'Y':
            return True
        else:
            return False

class Hand():
    '''
    Class presenting the hand of cards a player has
    ...
    ATTRIBUTES:
    -----------
    cards: list
        list of card objects
    value: int
        The sum of card objects a player has
    -----------
    Methods:
    -----------
    add_card()
        Add a card to the player's hand and update the hand's value
    __str__()
        prints the cards a player has
    '''
    def __init__(self):
        '''
        Parameters:
        -----------
        cards: str
            list of card objects the player has
        value: int
            The chips of cards in the player's hand
        '''
        self.cards = []
        self.value = 0
    def add_card(self, card):
        '''
        Add a card to the player's hand and update the hand's value
        -----------
        Parameters:
        -----------
        card: Card
            Card object to add to the player's hand
        '''
        self.cards.append(card)
        if card.rank == 'Ace':
            if self.value+11 > 21:
                card.value = 1
            else:
                card.value = 11
        self.value += card.value
    def __str__(self):
        '''
        Prints the cards a player has in the hand
        '''
        output = ''
        for card in self.cards:
            output += '\n'+ card.__str__()
        return output

def hit(hand):
    '''
    Add a new card to the player's hand after choosing to hit
    -----------
    Parameters:
    -----------
    hand: Hand
        The player's hand object to add cards to
    '''
    hand.add_card(deck.get_one_card())            

def player_action():
    '''
    Asks the player about the action to make in the game
    It can be:
        hit: Receive a new card
        Stand: Stop receiving cards
    '''    
    actions = ['Hit', 'Stand']
    action = ''
    while True:
        try:
            action = input("What do you want to do next?: Stand or Hit ")
            if action.capitalize() not in actions:
                print("This is blackjack! You can only hit or stand")
                continue
        except:
            print("Wrong input")
            continue
        else:
            print(f"Player has chosen to {action}")
            break
    if action.capitalize() == 'Hit':
        return True
    else:
        return False

def reset_game(hand):
    hand.value = 0
    hand.cards = []


if __name__ == "__main__":
    print("Welcome to Blackjack! The game where we take your money ;)")
    deck = Deck()
    deck.shuffle_deck()
    player = Player("You", 500)
    dealer = Player("Dealer", 500)
    hand_player = Hand()
    hand_dealer = Hand()
    gameon = True
    while gameon and player.chips:
        bet = player.bet()
        hand_player.add_card(deck.get_one_card())
        hand_player.add_card(deck.get_one_card())
        hand_dealer.add_card(deck.get_one_card())
        hand_dealer.add_card(deck.get_one_card())
        print(f"{dealer.name} has : \none hidden card \n"+hand_dealer.cards[0].__str__())
        print(f"{player.name} have :"+hand_player.__str__())
        while hand_player.value < 21:
            hit_action = player_action()
            if hit_action:
                hit(hand_player)
                print(hand_player)
            else:
                print(f"{player.name} have stood")
                break
        print(f"{player.name} have a hand of value: {hand_player.value}")
        if hand_player.value > 21:
            print(f"{player.name} have lost: BUST")
            player.lose_bet(bet)
            print(player)
            reset_game(hand_dealer)
            reset_game(hand_player)
            gameon = player.continue_playing()
            continue
        while hand_dealer.value < 17:
            hit(hand_dealer)
        print(hand_dealer)
        print(f"{dealer.name} has a hand of value: {hand_dealer.value}")
        if hand_dealer.value > 21:
            print(f"{dealer.name} has lost: BUST")
            dealer.lose_bet(bet)
            player.win_bet(bet)
            print(player)
            reset_game(hand_player)
            reset_game(hand_dealer)
            gameon = player.continue_playing()
            continue
        if hand_dealer.value <= 21 and hand_player.value <= 21:
            if hand_dealer.value > hand_player.value:
                print(f"{player.name} have lost")
                player.lose_bet(bet)
                print(player)
                reset_game(hand_dealer)
                reset_game(hand_player)
                gameon = player.continue_playing()
                continue
            elif hand_player.value > hand_dealer.value:
                print(f"{dealer.name} has lost")
                player.win_bet(bet)
                print(player)
                reset_game(hand_player)
                reset_game(hand_dealer)
                gameon = player.continue_playing()
                continue
            else:
                print("DRAW!")
                print(player)
                reset_game(hand_dealer)
                reset_game(hand_player)
                gameon = player.continue_playing()
                continue
    if not player.chips:
        print("You're broke, good luck next time")  
    else:
        print("See you next time, hope you enjoyed the game")      
