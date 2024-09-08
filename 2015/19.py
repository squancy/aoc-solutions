import re

def replacenth(string, sub, wanted, n):
    where = [m.start() for m in re.finditer(sub, string)][n-1]
    before = string[:where]
    after = string[where:]
    after = after.replace(sub, wanted, 1)
    newString = before + after
    return newString

def parse_input():
    repls = dict()
    s = None
    for line in open('19.txt').readlines():
        if '=>' in line:
            l, r = line.split('=>')
            if not l.strip() in repls:
                repls[l.strip()] = [r.strip()]
            else:
                repls[l.strip()].append(r.strip())
    else:
        s = line.strip()
    return repls, s

def first_part(repls, s):
    d = dict()
    for k in repls:
        for v in repls[k]:
            for i in range(s.count(k)):
                d[replacenth(s, k, v, i)] = 1 
    return len(d)

M = float('inf')
def find_path(repls, s, cur_str, num_of_steps, cache):
    print(cache)
    global M
    if cur_str == s:
        if num_of_steps < M:
            M = num_of_steps
        return num_of_steps
    elif not cur_str in cache and num_of_steps < M and len(cur_str) < len(s):
        cache[cur_str] = 1
        for k in repls:
            for v in repls[k]:
                for i in range(cur_str.count(k)):
                    find_path(repls, s, replacenth(cur_str, k, v, i), num_of_steps + 1, cache)
    return M

def second_part(repls, s):
    a = find_path(repls, s, 'e', 0, {})
    return M

repls, s = parse_input()
print('First part:', first_part(repls, s))
print('Second part:', second_part(repls, s))
