#   *******************************************************************************
#           |                   |                  |                     |
#   |                   |  ,-"_,=""     `"=.|                  |
#   |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#   _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
#   |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
#   |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#   _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
#   |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
#   |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
#   /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
#   ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
#   /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
#   /______/______/______/______/______/______/______/______/______/______/_____ /
#   *******************************************************************************

#Welcome to Treasure Island.
#Your mission is to find the treasure.
#You're at a cross road. Where do you want to go? Type "left" or "right" 

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
choose1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'")

if choose1 == 'left':
    choose2 = input("You've come to a lake. There is an island in the middle of the lake.Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    if choose2 == 'Wait':
        choose3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        if choose3 == 'Blue':
            print("You enter a room of beasts. Game Over.")
        elif choose3 == 'Red':
            print("It's a room full of fire. Game Over.")
        elif choose3 == "Yellow":
            print("You found the treasure! You Win!")
        else:
            print("Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")



