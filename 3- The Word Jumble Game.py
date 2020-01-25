# Word Jumble
# The computer picks a random word and jumbles it
# The player has to guess the original word
import random

# create a sequence of words to chose from
WORDS = ("python", "jumble", "easy", "difficult","answer","xylophone")

# pick randomly from WORDS
word = random.choice(WORDS)

# create a variable to see later if guess is right
correct=word

# create a jumbled version of the word
jumble=""

while word:
    position=random.randrange(len(word))
    jumble+=word[position]
    word=word[:position]+word[(position+1):]

# Welcoming the player
print('''
    Welcome to THE WORD JUMBLE
Unscramble the letters to make a word
Press Enter key at prompt to quit
''')

print("\nThe jumble is : ", jumble)

guess=input("\nYour guess : ")
guess=guess.lower()

while (guess!=correct) and (guess!=""):
    print("Sorry, that's not it.")
    guess = input("\nYour guess : ")
    guess = guess.lower()

if guess == correct:
    print("That's it! You guessed it!\n")

print("Thanks for playing.")
input("\n\nPress the enter key to exit.")