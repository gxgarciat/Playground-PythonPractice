# Type a program that will accept a two digits number and adds their digits together
# For example, if the input is 35, the output should be 3 + 5 = 8

# Input Block
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("")
print("***********************************")
print("            Let's start")
print("***********************************")
print("")


# Operation block
initialDirection = input("You are in front of a road. \nDo you want to go left or right? \n")
if initialDirection == "Right" or initialDirection == "right" :

    print("***********************************")
    print("            Game Over")
    print("***********************************")

else:
    print("")
    meanTransport = input("You just reached a lake. \nDo you want to go swim or wait? \n")
    if meanTransport == "Swim" or meanTransport == "swim" :
        print("***********************************")
        print("            Game Over")
        print("***********************************")
    else:
        print("")
        colorDoor = input("In front of you, there are three doors. \nChoose between the blue, red or the yellow door \n")
        if colorDoor == "blue" or colorDoor == "red":
            print("***********************************")
            print("            Game Over")
            print("***********************************")
        else:
            print("")
            print("***********************************")
            print("            You win")
            print("***********************************")


# Output block
