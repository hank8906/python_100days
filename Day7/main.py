import random
import life_stage
import hangman_words

end_game = False
#print starting logo
print (life_stage.logo)

# random choose a word in a list and break each letter into a list
word_list = hangman_words.word_list
word_chosen = random.choice(word_list)
word_chosen_list = list(word_chosen)
#print(word_chosen)


# add a '_' to each letter in the word chosen
display = []
for i in range(len(word_chosen)):
    display.append("_")

# while display stiil has '_'

life_count = len(life_stage.stages) -1
while display!= word_chosen_list:

    # let user guess a letter
    guess = input('please guess a letter: ').lower()  

    #if guess is in the word, change the blank in display for letter  
    for i in range(len(word_chosen)):
        if guess == word_chosen[i]:
            display[i] = guess

    # let user keep guessing until they guess the word
    if guess in word_chosen:
        print(display)
        if '_' not in display:
            print('You win')
    # if guess is not in the word
    else:
        print(f"You guess '{guess}',that's not in the word.You lose a life")
        print(display)
        print(life_stage.stages[life_count])
        
        if life_count != 0:
            life_count -= 1
        else:
            print('You lose')
            end_game = True
            break
        






