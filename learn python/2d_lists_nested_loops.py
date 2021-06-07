

# 2d list
number_grid = [
    # lists inside lists
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
# accessing list must specify index of row first and the index of item in list in second []
# print(number_grid[3][0])

for row in number_grid:
    #print(row)
    # col will return each element inside array
    for col in row:
        print(col)
