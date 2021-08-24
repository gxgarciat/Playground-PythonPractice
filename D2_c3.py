# Type a program that will calculate the amount of days, weeks and months left.
# This, assuming you will reach 90 years old.
# There are 365 days in a year, 52 weeks in a year and 12 months in a year.
# For example, you are 56 y.o., then you have 12410 days, 1768 weeks and 408 months left

# Variables block
totalDays = 365
totalWeeks = 52
totalMonths = 12

# Input block
userAge = float(input("What is your current age? \n"))

# Operations block
timeLeft = 90 - userAge
daysLeft = int(timeLeft * 365)
weeksLeft = int(timeLeft * totalWeeks)
monthsLeft = int(timeLeft * totalMonths)

# Output block
print(f"Your have {daysLeft} days, {weeksLeft} weeks and {monthsLeft} months left.")