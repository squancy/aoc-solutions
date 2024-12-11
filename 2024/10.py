grid = [[int(x) for x in line.strip()] for line in open("10.txt")]

def trailhead_score(i, j, reached):
    if grid[i][j] == 9 and not (i, j) in reached:
        reached.append((i, j))
        return 1
    res = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if (x == 0 and y == 0) or (x != 0 and y != 0):
                continue
            if 0 <= i + x < len(grid) and 0 <= j + y < len(grid[0]) and grid[i + x][j + y] - grid[i][j] == 1:
                res += trailhead_score(i + x, j + y, reached)
    return res

def trailhead_rating(i, j):
    if grid[i][j] == 9: 
        return 1
    res = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if (x == 0 and y == 0) or (x != 0 and y != 0):
                continue
            if 0 <= i + x < len(grid) and 0 <= j + y < len(grid[0]) and grid[i + x][j + y] - grid[i][j] == 1:
                res += trailhead_rating(i + x, j + y)
    return res

def first_part():
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                res += trailhead_score(i, j, [])
    return res

def second_part():
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                res += trailhead_rating(i, j)
    return res

print("First part:", first_part())
print("Second part:", second_part())
