# You are going to write a program that calculates the average student height from a List of heights.
# student_heights = [180, 124, 165, 173, 189, 169, 146]
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.

totalSum = 0
totalPopulation = 0
averageHeight = 0

# Input block
student_heights = input("Input a list of student heights: \n").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# Operations block
totalSum = sum(student_heights)
totalPopulation = len(student_heights)
averageHeight = round(totalSum/totalPopulation)

# Output block
print("")
print(f"The average height of the students is: {averageHeight}")
