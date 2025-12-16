def first_part():
    invs = []
    line = open("2.txt").readline()
    ranges = [[int(y) for y in x.split("-")] for x in line.split(",")]
    for rn in ranges:
        r = rn[0]
        if len(str(r)) % 2 == 0:
            inv = str(r)[:len(str(r)) // 2] * 2
        else:
            inv = ("1" + "0" * (len(str(r)) // 2)) * 2
        while int(inv) <= rn[1]:
            if rn[0] <= int(inv):
                invs.append(int(inv))
            inv = str(int(inv[:len(inv) // 2]) + 1) * 2
    return sum(invs)

def second_part():
    invs = []
    line = open("2.txt").readline()
    ranges = [[int(y) for y in x.split("-")] for x in line.split(",")]
    for rn in ranges:
        for n in range(rn[0], rn[1] + 1):
            for i in range(1, len(str(n)) // 2 + 1):
                if str(n)[:i] * (len(str(n)) // i) == str(n):
                    invs.append(n)
                    break
    return sum(invs)

print("First part:", first_part())
print("First part:", second_part())
