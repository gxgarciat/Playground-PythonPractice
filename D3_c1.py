# Write a program that indicates if a given number is odd or even
# Even numbers can be divide by 2 with no remainder
# For example, 86 is even as 86 / 2 = 43. This number does not have any decimal place

# Input block
userNumber = float(input("Write the number: \n"))

# Operations block
if userNumber % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")
