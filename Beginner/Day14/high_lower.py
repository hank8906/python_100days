import art
import game_data
import random

print(art.logo)

total_score = 0

while True:
    #start the game
    number1 = random.randint(0, len(game_data.data)-1)
    number2 = random.randint(0, len(game_data.data)-1)

    random_person1 = game_data.data[number1]
    random_person2 = game_data.data[number2]

    #list person1 and persons2's information 

    print(f"Compare A: {random_person1['name']}, {random_person1['description']}, {random_person1['country']}.")
    print(art.vs)
    print(f"Against B: {random_person2['name']}, {random_person2['description']}, {random_person2['country']}.")
    
    #ask the user to choose who has more followers
    choose = input("\nWho has more followers?Type 'A' or 'B': ")

    ## calculate score and compare the followers
    person_A = int(random_person1['follower_count'])
    person_B = int(random_person2['follower_count'])

    if choose == "A" or choose == "a":
        if person_A > person_B:
            total_score += 1
            print(f"You're right! Current score: {total_score}.")

        else:
            print(f"You're wrong! Current score: {total_score}.")
            total_score = 0
            continue_game = input("enter 'Y' to start again, or enter any key to leave: ")
            if continue_game != 'y' or continue_game != 'y':
                break

    elif choose == "B" or choose == "b":
        if person_A < person_B:
            total_score += 1
            print(f"You're right! Current score: {total_score}.")
        else:
            print(f"You're wrong! Current score: {total_score}.")
            total_score = 0
            continue_game = input("enter 'Y' to start again, or enter any key to leave: ")
            if continue_game != 'y' or continue_game != 'y':
                break

    
            



