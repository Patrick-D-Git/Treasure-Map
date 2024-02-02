line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]

treasure_map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Please provide positions from A to C, 1 to 3: ")

letter = position[0].upper()

if letter == "A":
    letter_position = 0
elif letter == "B":
    letter_position = 1
elif letter == "C":
    letter_position = 2
else:
    print("Incorrect Input. Please try again")
    exit()

print(letter_position)

number = int(position[1]) - 1

treasure_map[number][letter_position] = "X"


print(f"{line1}\n{line2}\n{line3}")
