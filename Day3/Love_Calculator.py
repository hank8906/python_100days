#Take both people's names and check for the number of times the letters in the word "TRUE" occurs. 
#Then check for the number of times the letters in the word "LOVE" occurs.
#Then combine these numbers to make a 2 digit number.
#-------------------------------------------------------------------------------------
#For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."

#For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together.

#"Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."
#-------------------------------------------------------------------------------------
# 1.Check the times that "TRUE" and "LOVE" occur in both name
# 2.remember the upperclass and lowerclass
# 3.Combine the two number into 2 digits
# 4.check the zone of the number in and print the answer
#-------------------------------------------------------------------------------------
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
count1 = 0
count2 = 0

letters1 = "TRUE"
letters2 = "LOVE"

for letter in name1:
    if letter.upper() in letters1:
        count1 += 1
    else:
        count1 += 0

for letter in name2:
    if letter.upper() in letters1:
        count1 += 1
    else:
        count1 += 0

for letter in name1:
    if letter.upper() in letters2:
        count2 += 1
    else:
        count2 += 0

for letter in name2:
    if letter.upper() in letters2:
        count2 += 1
    else:
        count2 += 0

total = int(str(count1) + str(count2))

if total < 10 or total> 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total > 40 and total < 50: 
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")