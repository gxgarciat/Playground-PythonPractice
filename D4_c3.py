# Write a program which will mark a spot with an X
# This program contains a nested list, as per the instruction
# Replace the grey box with an X, according to the coordinates

# Input block
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? \n")

# Operations block
horizontal = int(position[0])
vertical = int(position[1])

#selectedRow = map[vertical -1]
#selectedRow[horizontal-1] = "X"
map[vertical - 1][horizontal - 1] = "X"

# Output block
print("\n**************************************************")
print(f"    Your treasure is located as follows!")
print("**************************************************")

print(f"{row1}\n{row2}\n{row3}")
