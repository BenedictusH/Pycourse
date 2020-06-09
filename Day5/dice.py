import random
import time

again = "y"

print ('DICE ROLL SIMULATOR')
print ('-------------------')

while again != "n":
    rolls = int(input ('How many dice you wanna roll? '))

    for roll in range(rolls):
        counter = roll + 1
        result = random.randint(1, 6)
        print (f"Dice {counter} rolled a {result}!")
        time.sleep(0.5)

    again = input("Wanna do  it again (y/n)? ")

print ('Bye!')