def first_part():
    coords = [[int(x) for x in y.strip().split(",")] for y in open("9.txt").readlines()]
    print(coords)
    m = 0
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            a = (abs(coords[i][0] - coords[j][0]) + 1) * (abs(coords[i][1] - coords[j][1]) + 1)
            if a > m: m = a
    return m

def second_part():
    coords = [[int(x) for x in y.strip().split(",")] for y in open("9.txt").readlines()]

print("First part", first_part())
print("Second part", second_part())
