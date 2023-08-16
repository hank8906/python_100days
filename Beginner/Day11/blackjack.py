import art
import random

print(art.logo)

############### Blackjack Project #####################

#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.

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

############### Blackjack Game #####################
def Blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    Game_Ask = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if Game_Ask == 'n':
        exit()

    #Deal both user and computer a starting hand of 2 random card values.
    my_cards = []
    com_cards = []

    my_cards.append(random.choice(cards))
    my_cards.append(random.choice(cards))

    #If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
    my_scores = 0
    for card in my_cards:
        if card == 11 and (card + my_scores) < 21:
            my_scores += 11
        elif card == 11 and (card + my_scores) > 21:
            my_scores += 1
        else:
            my_scores += card

    print(f"Your cards: {my_cards}, current score : {my_scores}")

    com_cards.append(random.choice(cards))
    com_cards.append(random.choice(cards))

    #If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
    com_scores = 0
    for card in com_cards:
        if card == 11 and (card + com_scores) < 21:
            com_scores += 11
        elif card == 11 and (card + com_scores) > 21:
            com_scores += 1
        else:
            com_scores += card

    print(f"Computer's first cards is: {com_cards[0]}")

    #Detect when computer or user has a blackjack. (Ace + 10 value card).
    if com_scores == 21:
        print(f"Your final hand: {my_cards}, final score: {my_scores}")
        print(f"Computer's final hand: {com_cards}, final score: {com_scores}")
        print("Lose, opponent has Blackjack 😱")
        Blackjack()
        
    elif my_scores == 21 and com_scores != 21:
        print(f"Your final hand: {my_cards}, final score: {my_scores}")
        print(f"Computer's final hand: {com_cards}, final score: {com_scores}")
        print("Win, you has Blackjack 😱")
        Blackjack()

    #Ask the user if they want to get another card.
    Add_Card_Ask = 'y'
    while Add_Card_Ask == 'y':
        #if the user score is over 21, end the game
        if my_scores < 21: 
            Add_Card_Ask = input("Type 'y' to get another card, type 'n' to pass: ")
            if Add_Card_Ask == 'y':
                my_cards.append(random.choice(cards))
                if my_cards[-1] == 11 and (my_cards[-1]+ my_scores) < 21:
                    my_scores += 11
                elif my_cards[-1] == 11 and (my_cards[-1] + my_scores) > 21:
                    my_scores += 1
                else:
                    my_scores += my_cards[-1]
            print(f"Your cards: {my_cards}, current score: {my_scores}")
        else:
            print(f"Your final hand: {my_cards}, final score: {my_scores}")
            print(f"Computer's final hand: {com_cards}, final score: {com_scores}")
            print(f"You lose")
            Blackjack()

    print(f"Your final hand: {my_cards}, final score: {my_scores}")

    #Once the user is done and no longer wants to draw any more cards, let the computer play. 
    #The computer should keep drawing cards unless their score goes over 16.
    while com_scores < 16:
        com_cards.append(random.choice(cards))
        if com_cards[-1] == 11 and (com_cards[-1] + com_scores) < 21:
            com_scores += 11
        elif com_cards[-1] == 11 and (com_cards[-1] + com_scores) > 21:
            com_scores += 1
        else:
            com_scores += com_cards[-1]

    #Compare user and computer scores and see if it's a win, loss, or draw.
    if my_scores > com_scores and my_scores < 22 and com_scores < 22:
        print(f"Computer's final hand: {com_cards}, final score: {com_scores}")
        print(f"You win!")
        Blackjack()
    elif my_scores < com_scores and my_scores < 22 and com_scores < 22:
        print(f"Computer's final hand: {com_cards}, final score: {com_scores}")
        print(f"You lose!")
        Blackjack()
    elif my_scores > 21 and com_scores < 22:
        print(f"Computer's final hand: {com_cards}, final score: {com_scores}")
        print(f"You lose!")
        Blackjack()
    elif my_scores < 22 and com_scores > 21:
        print(f"Computer's final hand: {com_cards}, final score: {com_scores}")
        print(f"You win!")
        Blackjack()
    elif my_scores == com_scores:
        print(f"Computer's final hand: {com_cards}, final score: {com_scores}")
        print(f"Draw!")
        Blackjack()

#start the game
Blackjack()