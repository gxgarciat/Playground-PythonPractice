# Build a virtual coin toss program that will randomly tell the user "Heads" or "Tails"
# The first letter should be capitalised and spelt exactly like in the example

import random
coinTossed = 0

# Input block
print("Welcome to 'Heads' or 'Tails'")
print("Let's roll the dice!")

# Operations block
coinTossed = random.randint(0,1)
if coinTossed == 0:
    message = "Tails"
else:
    message = "Heads"

# Output block
print("\n****************************************")
print(f"        You got {message}.")
print("****************************************")
