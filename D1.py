# Create a greeting for your program
# Ask the user for the city that they grew up in
# Ask the user for the name of a pet
# Combine the name of their city and pet and show them their band name
# Make sure the input cursor shows on a new line, see the example at:

print("**Welcome to the Band Name Generator program**")

# Input - Name of the city
print("What is the name of the city you grew up in: ")
cityName = input()

# Input - Name of the pet
print("What is the name of your pet: ")
petName = input()

# Changing variables
cityName, petName = petName, cityName

# Showing results
print("The name of the band could be: " + cityName + " " + petName)
print()
print("**Thank you for using this app.**")