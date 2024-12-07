from functools import cmp_to_key

flag = True
deps = {}
orders = []
with open("5.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        if not line:
            flag = False
            continue
        if flag:
            x, y = [int(x) for x in line.split("|")]
            if x in deps:
                deps[x].add(y)
            else:
                deps[x] = set((y,))
        else:
            orders.append([int(x) for x in line.split(",")])  

def first_part():
    res = 0
    for order in orders:
        good_order = True
        for i in range(len(order)):
            if order[i] in deps and set(order[:i]) & deps[order[i]] != set():
                good_order = False
                break
        if good_order:
            res += order[i // 2]
    return res

def comp(x, y, order):
    if x in deps and y in deps[x]:
        return -1
    if y in deps and x in deps[y]:
        return 1
    return 0

def second_part():
    res = 0
    for order in orders:
        for i in range(len(order)):
            if order[i] in deps and set(order[:i]) & deps[order[i]] != set():
                res += sorted(order, key=cmp_to_key(lambda x, y: comp(x, y, order)))[len(order) // 2]
                break
    return res

print("First part:", first_part())
print("Second part:", second_part())

