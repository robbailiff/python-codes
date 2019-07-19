"""
I have developed an American Blackjack game using OOP and has Aces count as 1 or 11 (this was very tricky for me to work out).
Here are the general rules of the game:

    - The player aims to as close to 21 as possible  
    - The player can choose to hit (take a card) to improve their hand
    - If the player goes bust they lose  
    - The player can choose to stand (end their turn) and see how the dealer does
    - Dealer hits until he beats the player or goes bust

I have spent about a week testing and cleaning up the code and I think I've managed to get rid of most of the bugs.

"""

############################
##### American Blackjack ###
############################


# Import libraries
from random import choice
from time import sleep


###############
### Classes ###
###############

# Card class - with suit, rank and value attributes
class Card:

    def __init__(self):
        Card.suit = ["Hearts", "Diamonds", "Clubs", "Spades"] # List of suits
        Card.rank = ["2", "3", "4", "5", "6", "7", "8", "10", "J", "Q", "K", "A"] # List of ranks
        Card.value = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10,
                     "K": 10, "A": 1} # Dict of rank values (i.e. points)


# Deck class - create a 52 Deck
class Deck:

    def __init__(self):
        Deck.player_deck = []
        for s in Card.suit:
            for r in Card.rank:
                Deck.player_deck.append([r + ' of ' + s])


# Your hand class - set up your 2 cards at random
class Hand:

    def __init__(self):
        Hand.player_hand = []
        Hand.hand_value = 0
        Hand.ace_counter = 0

    def __str__(self):
        print(f"Your current hand is: \n{Hand.player_hand}")

    def draw_cards(self, number):
        for n in range(number):
            card = choice(Deck.player_deck)
            Deck.player_deck.remove(card)
            Hand.player_hand.append(card)

    def calculate_value(self):
        Hand.hand_value = 0
        Hand.ace_counter = 0    # Counts the number of aces in hand
        plus_counter = 0    # Counts when an ace value counts as 11

        for c in Hand.player_hand:
            for r in c:
                if 'A' in r:  # Ace value calculation
                    Hand.ace_counter += 1
                    p1_rank = str(r[0])
                    p1_value = Card.value[p1_rank]
                    Hand.hand_value = Hand.hand_value + int(p1_value)

                    for ace in range(Hand.ace_counter):
                        if Hand.hand_value <= 11:
                            Hand.hand_value += 10
                            plus_counter += 1

                elif '10' in r:  # 10s value calculation
                    p1_rank = str(r[0:2])
                    p1_value = Card.value[p1_rank]
                    Hand.hand_value = Hand.hand_value + int(p1_value)

                else:  # 1-9 value calculation
                    p1_rank = str(r[0])
                    p1_value = Card.value[p1_rank]
                    Hand.hand_value = Hand.hand_value + int(p1_value)

        if Hand.hand_value > 21 and plus_counter > 0:
            Hand.hand_value -= 10


# Dealer class fore handling dealer actions
class Dealer:

    def __init__(self):
        Dealer.dealer_hand = []
        Dealer.hand_value = 0
        Dealer.ace_counter = 0

    def draw_cards(self, number):
        for n in range(number):
            card = choice(Deck.player_deck)
            Deck.player_deck.remove(card)
            Dealer.dealer_hand.append(card)

    def dealer_value(self):
        Dealer.hand_value = 0
        Dealer.ace_counter = 0 # Counts the number of aces in hand
        plus_counter = 0 # Counts when an ace value counts as 11

        for c in Dealer.dealer_hand:
            for r in c:
                if 'A' in r:  # Ace value calculation
                    Dealer.ace_counter += 1
                    dealer_rank = str(r[0])
                    dealer_value = Card.value[dealer_rank]
                    Dealer.hand_value = Dealer.hand_value + int(dealer_value)

                    for ace in range(Dealer.ace_counter):
                        if Dealer.hand_value <= 11:
                            Dealer.hand_value += 10
                            plus_counter += 1

                elif '10' in r:  # 10s value calculation
                    dealer_rank = str(r[0:2])
                    dealer_value = Card.value[dealer_rank]
                    Dealer.hand_value = Dealer.hand_value + int(dealer_value)

                else:  # 1-9 value calculation
                    dealer_rank = str(r[0])
                    dealer_value = Card.value[dealer_rank]
                    Dealer.hand_value = Dealer.hand_value + int(dealer_value)

            if Dealer.hand_value > 21 and plus_counter > 0:
                Dealer.hand_value -= 10


# Chips (Bank acccount) class - add and subtract chips
class Chips:

    def __init__(self, player, total):
        self.player = player
        self.total = total

    def __str__(self):
        return f"Player: {self.player}\nNumber of chips: {self.total}"

    def deposit(self, amount):
        self.total = self.total + amount
        print(f"You have gained {amount} chips\n")

    def withdraw(self, amount):
        if amount > self.total:
            print("You are out of chips")
        else:
            self.total = self.total - amount
            print(f"You have bet {amount} chips\n")

#################
### Functions ###
#################

def play_again():
    if p1_chips.total == 0:
        game_active == False

    print("Would you like to play again?")
    while True:
        try:
            choice = int(input("Enter 1 for Yes or 2 for No: \n"))
            if choice == 1 or choice == 2:
                if choice == 1:
                    print("You have chosen to play another round\n")
                    return game_active == True
                    break

                elif choice == 2:
                    print("You have chosen to end the game")
                    return game_active == False
                    break

            else:
                print("That is not a valid number")
                continue

        except ValueError:
            print("You must enter a number")
            continue

###################
### Actual game ###
###################

# Initialise starting attributes
player_name = input("What is your name? ")
p1_chips = Chips(player_name, 1000)
game_active = True

######################
### Main game loop ###
######################

while game_active == True:
    # Initialise and reset deck and starting hands
    deck_cards = Card()
    main_deck = Deck()
    p1_hand = Hand()
    house_hand = Dealer()
    print(p1_chips)

    # Take bets (choose amounts)
    while True:
        try:
            bet = int(input("How much would you like to bet? "))
            p1_chips.withdraw(bet)
            break

        except ValueError:
            print("You must enter a number")
            continue

    # Player gets 2 cards face up
    p1_hand.draw_cards(2)
    print("You have drawn: ")
    print(f"{Hand.player_hand}\n")
    sleep(2)

    # Dealer gets 1 card face up and 1 card face down
    house_hand.draw_cards(2)
    print("The dealer has drawn: ")
    print(f"{Dealer.dealer_hand[1:]}\n")
    house_hand.dealer_value()
    sleep(2)

    # Player hand value
    p1_hand.calculate_value()
    print(f"Your current hand value is {Hand.hand_value}\n")

    ##############################
    ### Loop for hit and stand ###
    ##############################

    while p1_chips.total > 0 or Hand.hand_value <= 21 or Dealer.hand_value < 21:

        print("Press 1 to Hit or Press 2 to Stand")
        try:
            action = int(input("Would you like to Hit or Stand? \n"))
            if action == 1 or action == 2:
                if action == 1: # Hit
                    p1_hand.draw_cards(1)
                    print("You have drawn: ")
                    print(f"{Hand.player_hand}\n")
                    sleep(3)
                    p1_hand.calculate_value()

                    # If Hand value goes over 21, checks to revalue an Ace
                    if Hand.hand_value >= 21:
                        p1_hand.calculate_value()
                        # If hand value still over 21, break (and you lose)
                        if Hand.hand_value >= 21:
                            print(f"Your current hand value is {Hand.hand_value}\n")
                            break
                    else:
                        print(f"Your current hand value is {Hand.hand_value}\n")
                        continue

                elif action == 2: # Stand
                    print("You have chosen to Stand")
                    print(f"Your current hand value is {Hand.hand_value}\n")
                    break

            else:
                print("That is not a valid number")
                continue

        except ValueError:
            print("You must enter a number")
            continue

        ###################
        ### End of loop ###
        ###################

    ########################
    ### Dealer draw loop ###
    ########################

    while Dealer.hand_value < 21 or Dealer.hand_value < Hand.hand_value:

        # Win condition checks
        if p1_chips.total <= 0 or Hand.hand_value > 21: # Checks if player is bust or bankrupt
            break
        elif Dealer.hand_value > Hand.hand_value:   # Checks if dealer starter hand is larger
            print(f"The dealers current hand value is {Dealer.hand_value}\n")
            break
        elif Dealer.hand_value >= 21:   # Checks if the dealer has got 21 or gone bust
            print(f"The dealers current hand value is {Dealer.hand_value}\n")
            break

        # Dealer draws cards until loop is broken
        house_hand.draw_cards(1)
        print("The dealer has drawn: ")
        print(f"{Dealer.dealer_hand}\n")
        sleep(3)
        house_hand.dealer_value()
        print(f"The dealers current hand value is {Dealer.hand_value}\n")
        sleep(2)

    ###################
    ### End of loop ###
    ###################

    # Win or loss Conditions
    if Hand.hand_value == 21 and Dealer.hand_value != 21:
        print("You have scored 21!")
        print("You have won this round!")
        bet *= 2
        p1_chips.deposit(bet)

    if Hand.hand_value == 21 and Dealer.hand_value == 21:
        print("You and the dealer have both scored 21!")
        print("It is a draw this round!")
        p1_chips.deposit(bet)

    elif Hand.hand_value < 21 and Dealer.hand_value > 21:
        print("The dealer has gone bust!")
        print("You have won this round!")
        bet *= 2
        p1_chips.deposit(bet)

    elif Dealer.hand_value <= 21 and Dealer.hand_value > Hand.hand_value:
        print("You have lost this round!")

    elif Hand.hand_value > 21:
        print("You have gone bust!")

    elif p1_chips.total == 0:
        print ("You have ran out of chips!")

    play_again()

print("The game has ended")

###################
### END OF GAME ###
###################
