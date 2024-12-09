m = open("9.txt").readline().strip()

def decode(m):
    res = []
    idn = 0
    for i in range(len(m)):
        if i % 2 == 0:
            res.extend([idn for _ in range(int(m[i]))])
            idn += 1
        else:
            res.extend([None for _ in range(int(m[i]))])
    return res

def compress(m):
    m = m[:]
    bi = len(m) - 1
    si = 0
    while bi > si:
        while m[bi] == None:
            bi -= 1
            m.pop()
            if bi >= si: break
        while si < len(m) and m[si] != None:
            si += 1
        if si == len(m): break
        m[si] = m[bi]
        bi -= 1
        m.pop()
    return m

def find_si_block(bi_start, size, m):
    i = 0
    while i < len(m):
        if i >= bi_start: break
        sz = 0
        j = i
        while j < len(m) and m[j] == None:
            sz += 1
            j += 1
        if sz >= size:
            return i
        i += 1
    return None

def find_bi_block(bi, m):
    while m[bi] == None:
        bi -= 1
    e = bi
    while m[bi] != None and m[bi] == m[e]:
        bi -= 1
    return (bi + 1, e + 1, e - bi) 

def compress_block(m):
    m = m[:]
    bi_start = len(m) - 1
    si = 0
    while bi_start > 0:
        bi_start, bi_end, size = find_bi_block(bi_start, m)
        si = find_si_block(bi_start, size, m)
        if si != None:
            m[si:si + size] = m[bi_start:bi_end]
            m[bi_start:bi_end] = [None] * size
        bi_start -= 1
    return m

def solve(m):
    return sum([i * (m[i] if m[i] != None else 0) for i in range(len(m))])

print("First part:", solve(compress(decode(m))))
# kinda slow
print("Second part:", solve(compress_block(decode(m))))

