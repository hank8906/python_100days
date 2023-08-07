#rules
# 0 > 2, 0 < 1, 0 = 0
# 1 > 0, 1 < 2, 1 = 1 
# 2 > 1, 2 < 0, 2 = 2 

import random

my_choose = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
print(my_choose)

com_choose = random.randint(0,2)
print(com_choose)


# I am 0
if my_choose == 0 and com_choose == 2:
    print("You win")
elif my_choose == 0 and com_choose == 1:
    print("You lose")
elif my_choose == com_choose:
    print("Draw\nPlease try again")
else:
    print("please try again")

# I am 1
if my_choose == 1 and com_choose == 0:
    print("You win")
elif my_choose == 1 and com_choose == 2:
    print("You lose")
elif my_choose == com_choose:
    print("Draw\nPlease try again")
else:
    print("please try again")

# I am 2
if my_choose == 2 and com_choose == 1:
    print("You win")
elif my_choose == 2 and com_choose == 0:
    print("You lose")
elif my_choose == com_choose:
    print("Draw\nPlease try again")
else:
    print("please try again")
