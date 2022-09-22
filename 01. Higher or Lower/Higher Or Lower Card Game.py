# The game asks the player to predict whether the next card in the selection
# will have a higher ot lower value than the currently showing card.
# Rules:
#   If the player guesses correctly, they get 20 points.
#   If they choose incorrectly, they loose 15 points.
#   If the next card to be turned over has the same value as the previous card, the player is incorrect.
import random


def shuffle(deck):
    copied_deck = deck.copy()
    random.shuffle(copied_deck)
    return copied_deck


def choose_card(deck):
    return deck.pop()

# Main code
# 1. Preparation
print('Welcome to Higher or Lower.')
print("""You have to choose whether the next card to be shown 
will be higher or lower than the current card.
Getting it higher adds 20 points; get it wrong or if both cards are equal
and you loose 15 points.
You have 50 points to start.
****************************""")
POSSIBLE_SUITS = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
POSSIBLE_RANKS = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
NUM_OF_CARDS = 8
CARDS_LIST = []
card_points = 1
for suit in POSSIBLE_SUITS:
    for rank in POSSIBLE_RANKS:
        current_card = dict()
        current_card['rank'] = rank
        current_card['suit'] = suit
        current_card['value'] = card_points
        CARDS_LIST.append(current_card)
        card_points += 1
    card_points = 1

players_points = 50

# 2. Game starts
while True:
    # 2.1. Choosing the starting card
    shuffled_deck = shuffle(CARDS_LIST)
    chosen_card = choose_card(shuffled_deck)
    print(f"Your start card is {chosen_card['rank']} of {chosen_card['suit']} with a value of {chosen_card['value']}")
    # 2.1. Players input
    for i in range(NUM_OF_CARDS - 1):
        print("-" * 28)
        players_choice = input("Please, choose higher or lower by typing 'h' or 'l': ")
        previous_card = chosen_card['value']

        # 2.2 Choosing the nnext card
        shuffled_deck = shuffle(CARDS_LIST)
        chosen_card = choose_card(shuffled_deck)
        current_card = chosen_card['value']
        print(f"The drawn card is {chosen_card['rank']} of {chosen_card['suit']} with a value of {chosen_card['value']}")

        # 2.3 Checking whether the players choice has been right or wrong
        if players_choice == 'h':
            if current_card > previous_card:
                print("You got it right, it was higher")
                players_points += 20
            else:
                players_points -= 15
                print("Sorry, it was not higher")
        else:
            if current_card < previous_card:
                players_points += 20
                print("You got it right, it was lower")
            else:
                players_points -= 15
                print("Sorry, it was not lower")
        if players_points <= 0:
            print("Your points ended!")
            break
        print(f"Your score is: {players_points}")

    # 3. Continue to play or not
    play_again = input("Do you want to play again? (y/n): ")
    if play_again == 'y':
        continue
    else:
        print("Game Over!")
        break