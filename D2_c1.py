# Type a program that will accept a two digits number and adds their digits together
# For example, if the input is 35, the output should be 3 + 5 = 8

# Input block
number = input("Type a two digit number: \n")
number = float(number)

# Operations block
firstDig = number//10
secondDig = number%10
result = firstDig + secondDig
result = int(result)

# Output block
print(f"The result is {result}")