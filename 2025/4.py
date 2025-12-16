def at_least_four_nbors(i, j, grid):
    s = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if (x == i and y == j) or not (0 <= x < len(grid) and 0 <= y < len(grid[0])): continue
            s += grid[x][y]
    return s < 4

def first_part(grid):
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] and at_least_four_nbors(i, j, grid):
                res += 1
    return res

def second_part(grid):
    res = 0
    flag = True
    while flag:
        flag = False
        to_remove = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and at_least_four_nbors(i, j, grid):
                    res += 1
                    flag = True
                    to_remove.append((i, j))
        for r in to_remove:
            grid[r[0]][r[1]] = 0
    return res

grid = [[1 if c == "@" else 0 for c in line] for line in open("4.txt").readlines()]
print("First part:", first_part(grid))
print("Second part:", second_part(grid))
