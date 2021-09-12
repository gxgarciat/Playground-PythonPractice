# Build a program which will select a random name from a list of names
# The person selected will have to pay for everybody's food bill

import random
winnerBill = 0


# Input block
name_string = input("Give me everybody's names, separated by a comma. \n")
names = name_string.split(", ")


# Operations block
numberPart = len(names)

winnerBill = random.randint(0,numberPart-1)


# Output block
print("\n**************************************************")
print(f"  We have a winner! {names[winnerBill]} will pay the bill!")
print("*****************************************************")
