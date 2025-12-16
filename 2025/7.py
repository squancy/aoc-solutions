def splits(grid):
    split_below = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            split = False
            if i < len(grid) - 1:
                flag = False
                for k in range(i + 1, len(grid)):
                    if grid[k][j] == "^":
                        split_below[(i, j)] = [True, k]
                        flag = True
                        break
                if not flag:
                    split_below[(i, j)] = [False]
            else:
                split_below[(i, j)] = [False]
    return split_below

def calc_splits(split_below, cur_pos, cache):
    if not split_below[(cur_pos[0], cur_pos[1])][0]: return 0
    n = split_below[(cur_pos[0], cur_pos[1])][1]
    next_pos_1, next_pos_2 = (n, cur_pos[1] - 1), (n, cur_pos[1] + 1) 
    if (n, cur_pos[1]) in cache: return 0
    cache.append((n, cur_pos[1]))
    return 1 + calc_splits(split_below, next_pos_1, cache) + calc_splits(split_below, next_pos_2, cache)

def first_part():
    grid = [line.strip() for line in open("7.txt").readlines()]
    split_below = splits(grid)
    return calc_splits(split_below, (0, grid[0].index("S")), [])

def second_part():
    grid = [line.strip() for line in open("7.txt").readlines()]
    grid[-1] = "^" * len(grid[0])
    carets = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == "^"]
    carets = sorted(carets, key=lambda x: x[0])
    counts = {carets[0]: 1}
    for caret in carets[1:]:
        new_count = 0
        for i in range(caret[0] - 1, -1, -1):
            if (i, caret[1]) in carets: break
            if (i, caret[1] + 1) in carets:
                new_count += counts[(i, caret[1] + 1)]
            if (i, caret[1] - 1) in carets: 
                new_count += counts[(i, caret[1] - 1)]
        counts[caret] = new_count
     
    return sum([v for k, v in counts.items() if k[0] == len(grid) - 1])

print("First part:", first_part())
print("Second part:", second_part())
