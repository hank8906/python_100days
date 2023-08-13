import art
import re

#show the logo
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# ask the user whether to encode or decode, and the text and shift also
def ask_to_start():
    #ask for the direction
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction != "encode" and direction!= "decode":
        print("Invalid input, please try again.")
        ask_to_start()

    #ask for the text
    text = input("Type your message:\n").lower()
    if len(text) == 0 or text.isdigit() == True:
        print("Invalid input, please try again.")
        ask_to_start()
    
    #ask for the shift
    shift = int(input("Type the shift number:\n"))
    if shift < 0 or shift > 25:
        print("Invalid input, please try again.")
        ask_to_start()
    
    #call the function
    caesar(text,shift,direction)

#ask user if they want to continue
def ask_to_continue():
    answer = input("Type 'yes' to continue, type 'no' to quit:\n")
    if answer == "yes":
        ask_to_start()
    else:
        quit()

# caesar function
def caesar(text,shift,direction):
    # encode function
    if direction == "encode":
        cipher_text = ""
        for letter in text:
            if letter in alphabet:
                cipher_text += alphabet[(alphabet.index(letter) + shift) % 26]
            else:
                cipher_text += letter
        print(cipher_text)
        ask_to_continue()  

    # decode function
    else:
        plain_text = ""
        for letter in text:
            if letter in alphabet:
                plain_text += alphabet[(alphabet.index(letter) + 26 - shift) % 26]
            else:
                plain_text += letter
        print(plain_text)
        ask_to_continue()

# Start the program
ask_to_start()

