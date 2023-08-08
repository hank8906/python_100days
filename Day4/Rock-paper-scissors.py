#rules
# 0 > 2, 0 < 1, 0 = 0
# 1 > 0, 1 < 2, 1 = 1 
# 2 > 1, 2 < 0, 2 = 2 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

my_choose = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
print(my_choose)
if my_choose == 0:
    print(rock)
elif my_choose == 1:
    print(paper)
elif my_choose == 2:
    print(scissors)
else:
    print("please try again") 

com_choose = random.randint(0,2)
print(com_choose)
if com_choose == 0:
    print(rock)
elif com_choose == 1:
    print(paper)
elif com_choose == 2:
    print(scissors)
else:
    print("please try again") 


# I am 0
if my_choose == 0:
    if com_choose == 2:
        print("You win")
    elif com_choose == 1:
        print("You lose")
    elif my_choose == com_choose:
        print("Draw\nPlease try again")
    else:
        print("please try again")
elif my_choose == 1 :
    if com_choose == 0:
        print("You win")
    elif com_choose == 2:
        print("You lose")
    elif my_choose == com_choose:
        print("Draw\nPlease try again")
    else:
        print("please try again")
elif my_choose == 2:
    if com_choose == 1:
        print("You win")
    elif com_choose == 0:
        print("You lose")
    elif my_choose == com_choose:
        print("Draw\nPlease try again")
    else:
        print("please try again")
