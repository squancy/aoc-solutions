def first_part():
    rots = [line.strip() for line in open("1.txt").readlines()]
    pos = 50
    cnt = 0
    for rot in rots:
        if rot[0] == "L":
            pos -= int(rot[1:])
        else:
            pos += int(rot[1:])
        pos %= 100
        if pos < 0:
            pos = 100 + pos
        if pos == 0: cnt += 1
    return cnt

def second_part():
    rots = [line.strip() for line in open("1.txt").readlines()]
    pos = 50
    cnt = 0
    for rot in rots:
        if rot[0] == "L":
            turn = int(rot[1:])
            pos_s = pos
            if pos - turn <= 0:
                turn -= pos
                cnt += turn // 100 + (1 if pos_s != 0 else 0)
                pos = turn % 100
                if pos != 0: pos = 100 - pos
            else:
                pos -= int(rot[1:])
        else:
            pos += int(rot[1:])
            cnt += pos // 100
            pos %= 100
    return cnt

print("First part:", first_part())
print("Second part:", second_part())
