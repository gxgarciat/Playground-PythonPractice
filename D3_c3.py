# Write a program that will tell the user if a given year is a leap year
# For that purpose, the users needs to input the year and the program will decide if the information
# is or not a leap year.


# Input block
isLeapYear = int(input("Which year do you want to check? \n"))

# Operations block

lpChekOne = isLeapYear % 4
lpChekTwo = isLeapYear % 100
lpChekThree = isLeapYear % 400

if lpChekOne % 4 == 0:
    if lpChekTwo % 100 == 0:
        if lpChekThree % 400 == 0:
            finalMessage = "is a leap year."
        else:
            finalMessage = "is not a leap year."
    else:
        finalMessage = "is a leap year."
else:
    finalMessage = "is not a leap year."

# Output block
print("\n****************************************")
print(f"   The year {isLeapYear} {finalMessage}")
print("****************************************")