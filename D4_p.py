# Type a program that will play Rock, Paper, Scissors against the user
# Use the ASCII code to show the selection from the computer and the user

import random
computerRound = 0

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Input Block

print("Welcome to Rock, Paper, Scissors")

print("")
print("***********************************")
print("            Let's start")
print("***********************************")
print("")

userRound = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if userRound == 0:
    print(rock)
elif userRound == 1:
    print(paper)
else:
    print(scissors)

# Operation block
computerRound = random.randint(0,2)
print("Computer chose:")

if computerRound == 0:
    print("Rock")
    print(rock)
elif computerRound == 1:
    print("Paper")
    print(paper)
else:
    print("Scissors")
    print(scissors)

# Both are equal
if computerRound == userRound:
    print("***********************************")
    print("            Draw")
    print("***********************************")

# Rock wins against scissors
if computerRound == 0 and userRound == 2:
    print("***********************************")
    print("            Computer win")
    print("***********************************")
elif computerRound == 2 and userRound == 0:
    print("***********************************")
    print("            You win")
    print("***********************************")


# Paper wins against rock
if computerRound == 1 and userRound == 0:
    print("***********************************")
    print("            Computer win")
    print("***********************************")
elif computerRound == 0 and userRound == 1:
    print("***********************************")
    print("            You win")
    print("***********************************")

# Scissors win against paper
if computerRound == 2 and userRound == 1:
    print("***********************************")
    print("            Computer win")
    print("***********************************")
elif computerRound == 1 and userRound == 2:
    print("***********************************")
    print("            You win")
    print("***********************************")


# Output block
