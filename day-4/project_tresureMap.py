# 🚨 Don't change the code below 👇
row1 = ["100", "200", "300"]
row2 = ["400", "500", "600"]
row3 = ["700", "800", "900"]
# row3 = ["⬜","⬜","⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇 #23
column = int(position[0])  # 2
row = int(position[1])  # 3

selected_row = map[row - 1]
selected_row[column - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")