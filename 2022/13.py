from functools import cmp_to_key

def parse_line(line):
  if line.isnumeric():
    return int(line)

  arr = []
  parts = []
  level = 0
  breakpoints = [1]

  for i in range(1, len(line) - 1):
    was_zero = 1 if level == 0 else 0
    if line[i] == '[':
      level += 1
    elif line[i] == ']':
      level -= 1
    if was_zero and level != 0:
      breakpoints.append(i)
    elif not was_zero and level == 0:
      breakpoints.append(i + 1)
  
  breakpoints.append(len(line) - 1)

  for i in range(1, len(breakpoints)):
    parts.append(line[breakpoints[i - 1]:breakpoints[i]]) 

  for el in parts:
    if not el or el == ',':
      continue
    if not ('[' in el or ']' in el):
      for n in el.split(','):
        if not n:
          continue
        arr.append(parse_line(n))
    else:
      arr.append(parse_line(el))
  return arr

pairs = []
p = []
f = open('13.txt').readlines()
for i in range(len(f)):
  line = f[i].strip()
  if line:
    p.append(parse_line(line))
  if not line or i == len(f) - 1:
    pairs.append(p)
    p = []

def compare(p1, p2):
  if type(p1) == int and type(p2) == int:
    if p1 < p2:
      return -1
    elif p1 > p2:
      return 1
    return 0
  elif type(p1) == list and type(p2) == list:
    if len(p1) == 0 and len(p2) != 0:
      return -1
    elif len(p1) != 0 and len(p2) == 0:
      return 1
    elif len(p1) == 0 and len(p2) == 0:
      return 0
    c = compare(p1[0], p2[0])
    if c == 0:
      return compare(p1[1:], p2[1:])
    return c
  else:
    if type(p1) == int:
      i, l = [p1], p2
    else:
      i, l = p1, [p2]
    return compare(i, l)

def first_part(pairs):
  summa = 0
  for cnt, pair in enumerate(pairs):
    summa += cnt + 1 if compare(*pair) == -1 else 0
  return summa

def second_part(pairs):
  arr = [[[2]], [[6]]]
  for p in pairs:
    arr.extend(p)
  arr = sorted(arr, key=cmp_to_key(compare))
  return (arr.index([[2]]) + 1) * (arr.index([[6]]) + 1)

print('First part:', first_part(pairs))
print('Second part:', second_part(pairs))
