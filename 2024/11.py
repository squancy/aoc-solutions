from collections import defaultdict

stones = [int(x) for x in open("11.txt").readline().strip().split(" ")]
stones_d = defaultdict(int)
for x in open("11.txt").readline().strip().split(" "):
    stones_d[int(x)] = 1

def first_part():
    for _ in range(10):
        i = 0
        while i < len(stones):
            if stones[i] == 0:
                stones[i] = 1
            elif len(str(stones[i])) % 2 == 0:
                s = str(stones[i])
                stones[i:i+1] = [int(s[:len(s) // 2]), int(s[len(s) // 2:])]
                i += 1
            else:
                stones[i] *= 2024
            i += 1
    return len(stones)

def second_part(sd):
    for _ in range(75):
        x = list(sd.keys())
        sdc = sd.copy()
        if sd[0] != 0:
            sd[1] += sd[0]
            sd[0] = 0
        for k in x:
            if sdc[k] <= 0 or k == 0:
                continue
            if len(str(k)) % 2 == 0:
                s = str(k)
                sd[int(s[:len(s) // 2])] += sdc[k]
                sd[int(s[len(s) // 2:])] += sdc[k]
                sd[k] -= sdc[k]
            else:
                sd[k * 2024] += sdc[k]
                sd[k] -= sdc[k]
    return sum([sd[k] for k in sd if sd[k] > 0])
               
print("First part:", first_part())
print("Second part:", second_part(stones_d))
