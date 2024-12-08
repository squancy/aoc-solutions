from collections import defaultdict

d = {}
size = None
with open("8.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    size = (len(lines), len(lines[0]))
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != ".":
                if lines[i][j] in d:
                    d[lines[i][j]].append((i, j))
                else:
                    d[lines[i][j]] = [(i, j)]
def first_part():
    ants = defaultdict(tuple)
    for k in d:
        for i in range(len(d[k])):
            for j in range(i + 1, len(d[k])):
                m = (d[k][i][0] - d[k][j][0], d[k][i][1] - d[k][j][1])
                a1 = (d[k][i][0] + m[0], d[k][i][1] + m[1])
                a2 = (d[k][j][0] - m[0], d[k][j][1] - m[1])
                if 0 <= a1[0] < size[0] and 0 <= a1[1] < size[1]: ants[a1] = 1
                if 0 <= a2[0] < size[0] and 0 <= a2[1] < size[1]: ants[a2] = 1
    return len(ants)

def second_part():
    ants = defaultdict(tuple)
    for k in d:
        for i in range(len(d[k])):
            for j in range(i + 1, len(d[k])):
                m = (d[k][i][0] - d[k][j][0], d[k][i][1] - d[k][j][1])
                in_map = True
                l = 1
                ants[d[k][i]] = 1
                ants[d[k][j]] = 1
                while in_map:
                    in_map = False
                    a1 = (d[k][i][0] + l * m[0], d[k][i][1] + l * m[1])
                    a2 = (d[k][j][0] - l * m[0], d[k][j][1] - l * m[1])
                    if 0 <= a1[0] < size[0] and 0 <= a1[1] < size[1]:
                        ants[a1] = 1
                        in_map = True
                    if 0 <= a2[0] < size[0] and 0 <= a2[1] < size[1]:
                        ants[a2] = 1
                        in_map = True
                    l += 1
    return len(ants)

print("First part:", first_part())
print("Second part:", second_part())
