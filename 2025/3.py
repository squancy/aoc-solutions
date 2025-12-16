def first_part():
    lines = [line.strip() for line in open("3.txt").readlines()]
    res = 0
    for line in lines:
        f = max([int(x) for x in line[:-1]])
        s = max([int(x) for x in line[line.index(str(f)) + 1:]])
        res += int(str(f) + str(s))
    return res

def second_part():
    lines = [line.strip() for line in open("3.txt").readlines()]
    res = 0
    for line in lines:
        num = ""
        prev_start = 0
        for i in range(12):
            end = -(11 - i) if 11 - i > 0 else len(line)
            m = max([int(x) for x in line[prev_start:end]])
            num += str(m)
            prev_start = prev_start + line[prev_start:end].index(str(m)) + 1
        res += int(num)
    return res

print("First part:", first_part())
print("First part:", second_part())
