# This program takes a list of lists and prints it out.
#
# This is sort of like printing a bitmap in a very simple
# manner.

# The grid is copy-pasted straight from the webpage. When
# it prints, it will print an ASCII-art heart. 
#
# The x-axis value of this is len(grid) and the y value
# is going to be len(grid[0]). So the first line of the
# picture is in the [0] element of each grid[i] element.
# The next line is in [1], and so on. 
# 
# It's easier to do than it is to explain.

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for x in range(len(grid[0])):
    for y in range(len(grid)):
        print(grid[y][x], end = "")
    print("")

