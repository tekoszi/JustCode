import itertools

grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 0, 0]]

def possible(y,x,n):
    global grid
    for i in range(9):
        if grid[y][i] == n:
            return False
    for i in range(9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i, j in itertools.product(range(3), range(3)):
        if grid[y0+i][x0+j] == n:
            return False
    return True
# print(possible(4,4,5))

def solve():
    # print('solve')
    global grid
    for x, y in itertools.product(range(9), range(9)):
        if grid[y][x] == 0:
            for n in range(1,10):
                if possible(y,x,n):
                    grid[y][x] = n
                    solve()
                    grid[y][x] = 0
            return
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in grid]))
    print('\n\n')

solve()
# print(grid)