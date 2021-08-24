# Write a program that will calculate the BMI
# For that purpose, the users needs to input their weight and height
# For example, w= 80 & height = 1.75, the output will be 26
# In addition, if the BMI is under 18.5, the program will tell the user they are underweight
# if the BMI is over 18.5 but below 25, the program will tell the user they have normal weight
# if the BMI is over 25 but below 30, the program will tell the user they are overweight
# if the BMI is over 30 but below 35, the program will tell the user they are obese
# if the BMI is over 35, the program will tell the user they are clinically obese

# Input block
height = float(input("Enter your height in [m]: \n"))
weight = float(input("Enter your weight in [kg]: \n"))

# Operations block
bmiCalc = weight/(height*height)
bmiCalc = round(bmiCalc,0)

if bmiCalc <= 18.5:
    medDescrip = "you are underweight."
elif 18.5 < bmiCalc <= 25:
    medDescrip = "you have a normal weight."
elif 25 < bmiCalc <= 30:
    medDescrip = "you are overweight."
elif 30 < bmiCalc <= 35:
    medDescrip = "you are obese."
else:
    medDescrip = "you are clinically obese."

# Output block

print("\n****************************************")
print(f"Your BMI is: {bmiCalc}, {medDescrip}")
print("****************************************")