import re

s = ''.join([x.strip() for x in open("3.txt").readlines()])

def first_part(s):
    return sum([int(x[0]) * int(x[1]) for x in re.findall(r'mul\(((?:\d){1,3}),((?:\d){1,3})\)', s)])

def second_part(s):
    start = 0
    flag = 1
    i = 0
    res = 0
    while i < len(s):
        if s[i:].startswith("don't()") or i == len(s) - 1:
            if i == len(s) - 1: i += 1
            if flag:
                res += first_part(s[start:i])
            i += 7
            start = i
            flag = 0
        elif s[i:].startswith("do()"):
            if not flag:
                start = i + 4
            flag = 1
            i += 1
        else:
            i += 1
    return res 

print("First part:", first_part(s))
print("Second part:", second_part(s))
