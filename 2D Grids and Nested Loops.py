#06/12/2022

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
#making all items in the number grid lists as lists

print(number_grid[0][1])

for row in number_grid:
    for col in row:#printing the columns per row for individuals
        print(col)
