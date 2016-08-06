'''
char_pic_grid.py -- print characters in grid list as:
    ..oo.oo..
    .ooooooo.
    .ooooooo.
    ..ooooo..
    ...ooo...
    ....o....
'''

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'o', 'o', '.', '.', '.'],
        ['o', 'o', 'o', 'o', '.', '.'],
        ['o', 'o', 'o', 'o', 'o', '.'],
        ['.', 'o', 'o', 'o', 'o', 'o'],
        ['o', 'o', 'o', 'o', 'o', '.'],
        ['o', 'o', 'o', 'o', '.', '.'],
        ['.', 'o', 'o', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for i in range(len(grid[0])):
    for j in range(len(grid)):
        print(grid[j][i], end='')
    print()
