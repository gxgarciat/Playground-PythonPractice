# Build a program that create an automatic pizza order
# Consider that there are three types of pizza: Small ($15), Medium ($20) and large ($25)
# If you want to add pepperoni, you will need to add $2 for a small pizza
# For the Medium or large one, you will need to add $3
# If you want extra cheese, the added price will be $1, for any size

totalBill = 0

# Input block
print("Welcome to Python Pizza Deliveries!")
pizzaSize = input("What size of pizza do you want? S, M L \n")
pepperoniOption = input("Do you want pepperoni? Y, N \n")
extraCheese = input("Do you want extra cheese? Y, N \n")

# Operations block
smallP = 15
mediumP = 20
largeP = 25

if pizzaSize == "S":
    totalBill = totalBill + smallP
    if pepperoniOption == "Y":
        totalBill = totalBill + 2
elif pizzaSize == "M":
    totalBill = totalBill + mediumP
else:
    totalBill = totalBill + largeP

if pepperoniOption == "Y" and pizzaSize != "Y":
    totalBill = totalBill + 3

if extraCheese == "Y":
    totalBill = totalBill + 1

totalBill = round(totalBill,2)

# Output block
print("\n****************************************")
print(f"   The final bill is ${totalBill}.")
print("****************************************")