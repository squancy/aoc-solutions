import re

def gen_nums(s):
  d = {}
  for p in s:
    if p:
      for x in p.split(' '):
        if x: d[int(x.strip())] = 1
  return d

def parse_input():
  c = re.compile('Card\s+\d+:\s*((?:\d+\s+)+)\s*|\s*((?:\d+\s+)+)')
  d = []
  for line in open('4.txt').readlines():
    s = re.findall(c, line.strip() + ' ') 
    d.append([gen_nums(s[0]), gen_nums(s[1]), 1])
  return d

def first_part(inp):
  total = 0
  for v in inp:
    cnt = 0
    for poss in v[1].keys():
      if poss in v[0]:
        cnt += 1
    total += 2 ** (cnt - 1) if cnt >= 1 else 0
  return total

def second_part(inp):
  for i, v in enumerate(inp):
    cnt = 0
    for poss in v[1].keys():
      if poss in v[0]:
        cnt += 1  
    for j in range(1, cnt + 1):
      inp[i + j][2] += inp[i][2]
  return sum(x[2] for x in inp)

inp = parse_input()
print('First part:', first_part(inp))
print('Second part:', second_part(inp))
