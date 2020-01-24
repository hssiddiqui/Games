# Guess my number
# The computer picks a random number between 1 and 100
# The player tries to guess it and
# the computer lets the player know if the guess is too high or too low or right on the money

import random

print('''
Welcome to guess my number
I'm thinking of a number between 1 and 100
Try to guess it in as few attempts as possible. \n''')

# set the initial values
the_number=random.randrange(100)+1
guess=int(input("Take a guess: "))
tries=1

# guessing loop
while (guess != the_number):
    if (guess > the_number):
        print("Lower...")
    else:
        print("Higher...")

    guess = int(input("Take a guess: "))
    tries+=1

print("You guessed it! The number was ", the_number)
print("It only took you ", tries, "tries!\n")

input("\n\nPress the enter key to exit")

print('''
   ____         ____       ___   ___   _______
 /  ___ \      /    |     /   | /   | |  _____|
|  |          / / | |    / /|    /| | | |_____
|  |   __    /  __  |   / / |___/ | | |  _____|
|  |__|  |  / /   | |  / /        | | | |_____
 \______/  /_/    |_| /_/         |_| |_______|
   ____     _      _  ________   ______
 /  __  \\  | |   / / |  ______| |  ___  \\
|  |  |  | | |  / /  | |______  | |___| |
|  |  |  | | | / /   |  ______| |  ___  /
|  |__|  | | |/ /    | |______  | |   \ \\
 \______/  |___/     |________| |_|    \_\\
''')