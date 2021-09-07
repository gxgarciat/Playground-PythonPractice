# Build a program that tests the compatibility between people
# For that, you need to check the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs. then combine these numbers to make
# a 2 digit number
# If you want extra cheese, the added price will be $1, for any size
# Finally, for Love Scores less than 10 or greater than 90, the message should be: you go together like coke and mentos
# between 40 and 50, you are alright together. Otherwise, the message should be just their score.

digitOne = 0
digitTwo = 0
firstLetter = 0
secondLetter = 0
thirdLetter = 0
fourthLetter = 0


# Input block

print("Welcome to the compatibility love test!")
loverOne = input("What is your name? \n")
loverTwo = input("What is their name? \n")

loverOne = loverOne.lower()
loverTwo = loverTwo.lower()


# Operations block
firstLetter = loverOne.count("t") + loverTwo.count("t")
secondLetter = loverOne.count("r") + loverTwo.count("r")
thirdLetter = loverOne.count("u") + loverTwo.count("u")
fourthLetter = loverOne.count("e") + loverTwo.count("e")

digitOne = firstLetter + secondLetter + thirdLetter + fourthLetter

firstLetter = loverOne.count("l") + loverTwo.count("l")
secondLetter = loverOne.count("o") + loverTwo.count("o")
thirdLetter = loverOne.count("v") + loverTwo.count("v")
fourthLetter = loverOne.count("e") + loverTwo.count("e")

digitTwo = firstLetter + secondLetter + thirdLetter + fourthLetter

score = digitOne * 10 + digitTwo

if score < 50 and score > 40:
    finalMessage = ", you are alright together."
elif 10 > score or score > 90:
    finalMessage = ", you go together like coke and mentos."
else:
    finalMessage = "."


# Output block
print("\n****************************************")
print(f"   Your score is {score}{finalMessage}")
print("****************************************")
