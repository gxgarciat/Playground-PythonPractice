# Type a program that will calculate the BMI
# For that purpose, the users needs to input their weight and height
# For example, w= 80 & height = 1.75, the output will be 26

# Input block
height = float(input("Enter your height in [m]: \n"))
weight = float(input("Enter your weight in [kg]: \n"))

# Operations block
bmiCalc = weight/(height*height)
bmiCalc = round(bmiCalc,0)

# Output block
print(f"Your BMI is: {bmiCalc}")