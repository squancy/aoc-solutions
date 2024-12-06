grid = [x.strip() for x in open('4.txt').readlines()]

pattern = 'XMAS'

def hor(i, j, m):
    for k in range(1, 4):
        try:
            if grid[i][j + m * k] != pattern[k] or j + m * k < 0:
                return 0
        except IndexError:
            return 0
    return 1

def ver(i, j, m):
    for k in range(1, 4):
        try:
            if grid[i + m * k][j] != pattern[k] or i + m * k < 0:
                return 0
        except IndexError:
            return 0
    return 1

def diag(i, j, m1, m2):
    for k in range(1, 4):
        try:
            if grid[i + m1 * k][j + m2 * k] != pattern[k] or i + m1 * k < 0 or j + m2 * k < 0:
                return 0
        except IndexError:
            return 0
    return 1

def first_part():
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'X':
                for m in [-1, 1]:
                    res += hor(i, j, m)
                    res += ver(i, j, m)
                for m in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    res += diag(i, j, *m)
    return res

def second_part():
    res = 0
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            d1 = grid[i - 1][j - 1] + grid[i][j] + grid[i + 1][j + 1]
            d2 = grid[i - 1][j + 1] + grid[i][j] + grid[i + 1][j - 1]
            if (d1 == "MAS" or d1[::-1] == "MAS") and (d2 == "MAS" or d2[::-1] == "MAS"):
                res += 1
    return res

print("First part:", first_part())
print("Second part:", second_part())
