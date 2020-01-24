name=input("What is your name? ")
age=input("How old are you? ")
age=int(age)
weight=input("How many pounds do you weigh? ")
weight=int(weight)

print("\nIf poet ee cummings were to email you, he'd address you as", name.lower())
ee_mad=name.upper()
print("\nBut if ee were mad, he'd call you", ee_mad)

dog_years=age/7
print("\nDid you know that you're just ", dog_years," in dog years?")

seconds=age*365*24*60*60
print("\nBut you're also over ", seconds," seconds old.")

moon_weight = weight/6.0
print("\nDid you know that on the moon you would weigh only ", moon_weight," pounds?")

sun_weight = weight*27.1
print("\nBut on the sun you'd weigh ", sun_weight," (but, aah... not for long)")


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
