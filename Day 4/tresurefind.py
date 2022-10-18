
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
#holding position

#horizontal
c = int(position[0])
#vertical
r = int(position[1])

map[r-1][c-1] = "x"

print(f"{row1}\n{row2}\n{row3}")
