# Hangman Game

import random

# constants

HANGMAN=(
    """
     ----
    |    |
    |
    |
    |
    |
    |
    |
    |
____________    
    """,
    """
     ----
    |    |
    |    0
    |
    |
    |
    |
    |
    |
____________    
    """,
    """
     ----
    |    |
    |    0
    |   -+-
    |
    |
    |
    |
    |
____________    
    """,
    """
     ----
    |    |
    |    0
    |  /-+-
    |
    |
    |
    |
    |
____________    
    """,
    """
     ----
    |    |
    |    0
    |  /-+-/
    |
    |
    |
    |
    |
____________    
    """,
    """
     ----
    |    |
    |    0
    |  /-+-/
    |    |
    |
    |
    |
    |
____________    
    """,
    """
     ----
    |    |
    |    0
    |  /-+-/
    |    |
    |    |
    |    |
    |    |
    |
____________    
    """,
    """
     ----
    |    |
    |    0
    |  /-+-/
    |    |
    |    |
    |   | |
    |   | |
    |
____________    
    """)

MAX_WRONG = len(HANGMAN)-1

WORDS = ("SOLAR", "WIND", "RIGS", "OFFSHORE", "ELECTRIFICATION", "RENEWABLES", "GRID")

# Initialization
word=random.choice(WORDS)
so_far = "-"*len(word)
wrong = 0   # number of wrong guesses
used = []   # letters guessed


print("Welcome to HANGMAN")

while wrong < MAX_WRONG and so_far!=word:
    print (HANGMAN[wrong])
    print ("\nYou've used the following letters:\n",used)
    print("\nSo far the word is:\n",so_far)



    guess = input("\n\nEnter your guess: ")
    guess=guess.upper()

    while guess in used:
        print("You've already guessed the letter: ", guess)
        guess = input("Enter your guess: ")
        guess = guess.upper()

    used.append(guess)



    if guess in word:
        print("\nYes! ", guess," is in word!")

        #create a new so_far to include guess
        new = ""
        for i in range((len(word))):
            if guess == word[i]:
                new += guess
            else:
                new+= so_far[i]
        so_far = new

    else:
        print("\nSorry, ",guess," isn't in the word.")
        wrong+=1



# Ending the game
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou've been hanged!")
else:
    print("\nYou guessed it!")

print("\nThe word was ",word)

input("\n\nPress the enter key to exit.")
