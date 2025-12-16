import math

def first_part():
    res = 0
    cols = parse()
    for k, v in cols.items():
        if v[-1] == "*":
            res += math.prod(v[:-1]) 
        else:
            res += sum(v[:-1])
    return res

def parse():
    cols = {}
    for line in open("6.txt").readlines():
        try:
            n = " ".join(line.split()).split(" ")
            nums = [int(x) for x in n]
        except Exception:
            nums = [x.strip() for x in n]
        for i in range(len(nums)):
            if i in cols: cols[i].append(nums[i])
            else: cols[i] = [nums[i]]
    return cols

def second_part():
    grid = [line.replace("\n", "") for line in open("6.txt").readlines()]
    cols = parse()
    res = 0
    col_cnt = 0
    for i in range(len(grid[-1])):
        if grid[-1][i] != " ":
            cols[col_cnt].append(True)
            for j in range(2, len(grid) + 1):
                if grid[-j][i] == " ":
                    cols[col_cnt][-1] = False
                    break
            col_cnt += 1
    for i in range(len(cols)):
        max_len = max(len(str(cols[i][k])) for k in range(len(cols[i]) - 2))
        if cols[i][-1]:
            for j in range(len(cols[i]) - 2):
                cols[i][j] = str(cols[i][j]) + "x" * (max_len - len(str(cols[i][j])))
        else:
            for j in range(len(cols[i]) - 2):
                cols[i][j] = "x" * (max_len - len(str(cols[i][j]))) + str(cols[i][j])
    
    for i in range(len(cols)):
        nums = {}
        for j in range(len(cols[i][0])):
            for k in range(len(cols[i]) - 2):
                if j in nums: nums[j] += cols[i][k][j]
                else: nums[j] = cols[i][k][j]
        ns = [int(n.replace("x", "")) for n in nums.values()]
        if cols[i][-2] == "+":
            res += sum(ns)
        else:
            res += math.prod(ns)
    return res 

print("First part", first_part())
print("Second part", second_part())
