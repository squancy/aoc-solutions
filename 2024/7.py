d = {}
with open("7.txt") as f:
    for line in f.readlines():
        o, t = line.split(": ")
        d[int(o)] = [int(x) for x in t.split(" ")]

def is_possible(cur_val, i, k):
    if cur_val > k or (cur_val < k and i == len(d[k])):
        return set()
    elif cur_val == k and i == len(d[k]):
        return set([k])
    return is_possible(cur_val + d[k][i], i + 1, k) | is_possible(cur_val * d[k][i], i + 1, k)

def is_possible_3(cur_val, i, k):
    if cur_val > k or (cur_val < k and i == len(d[k])):
        return set()
    elif cur_val == k and i == len(d[k]):
        return set([k])
    return is_possible_3(cur_val + d[k][i], i + 1, k) | is_possible_3(cur_val * d[k][i], i + 1, k) | is_possible_3(int(str(cur_val) + str(d[k][i])), i + 1, k)

def solve(f):
    res = set()
    for k in d:
        res |= f(d[k][0], 1, k)
    return sum(res)

print("First part:", solve(is_possible))
print("Second part:", solve(is_possible_3))

