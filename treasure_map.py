line1 = ["⬜️️","⬜️️","⬜️️","⬜️️","⬜️️","⬜️️"]
line2 = ["⬜️️","⬜️️","⬜️️","⬜️️","⬜️️","⬜️️"]
line3 = ["⬜️️","⬜️️","⬜️️","⬜️️","⬜️️","⬜️️"]
line4 = ["⬜️️","⬜️️","⬜️️","⬜️️","⬜️️","⬜️️"]
line5 = ["⬜️️","⬜️️","⬜️️","⬜️️","⬜️️","⬜️️"]
line6 = ["⬜️️","⬜️️","⬜️️","⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3, line4, line5, line6]
print("\nHiding your treasure! X marks the spot.\n")
position = input("Where do you want to put the treasure?\n")


first = position[0].lower()
second = int(position[1])-1
first_letter = ["a", "b", "c", "d", "e", "f"]
map_first = first_letter.index(first)
map[second][map_first] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}\n{line4}\n{line5}\n{line6}")