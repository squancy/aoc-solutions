def d(x, y):
    return sum([(x[i] - y[i]) ** 2 for i in range(3)]) ** 0.5

def first_part():
    coords = [tuple(int(x) for x in y.strip().split(",")) for y in open("8.txt").readlines()]
    dists = {}
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            dists[(coords[i], coords[j])] = d(coords[i], coords[j])
    dists = {k: v for k, v in sorted(dists.items(), key=lambda item: item[1])}
    groups = {coord: 0 for coord in coords}
    it = iter(dists)
    c = 1
    for i in range(1000):
        x = next(it)
        if groups[x[0]] == 0 and groups[x[1]] == 0:
            groups[x[0]] = groups[x[1]] = c
            c += 1
        elif groups[x[0]] == 0 and groups[x[1]] != 0:
            groups[x[0]] = groups[x[1]]
        elif groups[x[0]] != 0 and groups[x[1]] == 0:
            groups[x[1]] = groups[x[0]]
        elif groups[x[0]] != groups[x[1]]:
            gs = groups[x[0]]
            for k, v in groups.items():
                if v == gs:
                    groups[k] = groups[x[1]]
    gvals = set(groups.values())
    res = {}
    for gval in gvals:
        for _, v in groups.items():
            if v == gval:
                res[gval] = res.get(gval, 0) + 1
    del res[0]
    res = {k: v for k, v in sorted(res.items(), key=lambda item: item[1], reverse=True)}
    it = iter(res.values())
    return next(it) * next(it) * next(it)

def second_part():
    coords = [tuple(int(x) for x in y.strip().split(",")) for y in open("8.txt").readlines()]
    dists = {}
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            dists[(coords[i], coords[j])] = d(coords[i], coords[j])
    dists = {k: v for k, v in sorted(dists.items(), key=lambda item: item[1])}
    groups = {coord: 0 for coord in coords}
    it = iter(dists)
    c = 1
    while True:
        x = next(it)
        if groups[x[0]] == 0 and groups[x[1]] == 0:
            groups[x[0]] = groups[x[1]] = c
            c += 1
        elif groups[x[0]] == 0 and groups[x[1]] != 0:
            groups[x[0]] = groups[x[1]]
        elif groups[x[0]] != 0 and groups[x[1]] == 0:
            groups[x[1]] = groups[x[0]]
        elif groups[x[0]] != groups[x[1]]:
            gs = groups[x[0]]
            for k, v in groups.items():
                if v == gs:
                    groups[k] = groups[x[1]]
        if len(set(groups.values())) == 1:
            return x[0][0] * x[1][0]

print("First part", first_part())
print("Second part", second_part())
