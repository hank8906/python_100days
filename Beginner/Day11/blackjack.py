import art
import random

print(art.logo)

############### Blackjack Project #####################
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

############### Blackjack Game #####################

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

Game_Ask = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

# while Game_Ask == 'y':

#Deal both user and computer a starting hand of 2 random card values.
my_cards = []
com_cards = []

my_cards.append(random.choice(cards))
my_cards.append(random.choice(cards))

my_scores = 0
for card in my_cards:
    if card == 11 and my_scores < 21:
        my_scores += 11
    elif card == 11 and my_scores > 21:
        my_scores += 1
    else:
        my_scores += card

print(f"Your cards: {my_cards}, current score : {my_scores}")

com_cards.append(random.choice(cards))
com_cards.append(random.choice(cards))
com_scores = 0
for card in com_cards:
    com_scores += card

print(f"Computer's first cards is: {com_cards[0]}")

#Detect when computer or user has a blackjack. (Ace + 10 value card).
if com_scores == 21:
    print(f"Your final hand: {my_cards}, final score: {my_scores}")
    print(f"Computer's final hand: {com_cards}, final score: {com_scores}")
    print("Lose, opponent has Blackjack 😱")
elif my_scores == 21 and com_scores != 21:
    print(f"Your final hand: {my_cards}, final score: {my_scores}")
    print(f"Computer's final hand: {com_cards}, final score: {com_scores}")
    print("Win, you has Blackjack 😱")




