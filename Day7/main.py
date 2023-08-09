import random

word_list = ["aardvark", "baboon", "camel"]

#TODO: 1- Randomly choose a word from the word_list and assign it to a variable called chosen_word.

word_chosen = random.choice(word_list)
print(word_chosen)

#TODO: - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input('please guess a letter: ').lower()  

#TODO: - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

if guess in word_chosen:
    print("Yes, it's in the word")
else:
    print(f"You guess '{guess}',that's not in the word.You lose a life")



