# Type a program that will work as a tip calculator
# First, the user will need to type the bill. Second, the program will ask the percentage of tip
# Finally, the program will ask how many people to split the bill and it will provide how much each person should pay
# For example, the bill is $124.56, then you want to tip 12% and split into 7. Each person should pay 19.93

# Variables block

# Input block
print("Welcome to the tip calculator")
totalBill = float(input("What was the total bill? \n$ "))
tipPercentage = float(input("What percentage tip would you like to give? 10 12 or 15? \n"))
totalPeople = int(input("How many people to split the bill? \n"))

# Operations block
billSplit = round((totalBill * (1 + tipPercentage/100)) / totalPeople,2)

# Output block
print(f"Each person should pay: ${billSplit}")