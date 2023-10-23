import re, math

def parse_input():
  d = {}
  p = re.compile('(\w+): capacity (-|)(\d+), durability (-|)(\d+), flavor (-|)(\d+), texture (-|)(\d+), calories (-|)(\d+)')
  for line in open('inp15.txt').readlines():
    s = re.search(p, line) 
    if s:
      d[s.group(1)] = []
      for i in range(3, 13, 2):
        d[s.group(1)].append(int(s.group(i - 1) + s.group(i)))
  return d

def rec(l, tp, d, typ):
  if (len(tp) == l and sum(tp) != 100) or (sum(tp) > 100):
    return 0
  elif len(tp) == l:
    prod = 1
    for i in range(len(d[list(d.keys())[0]]) - 1):
      s = 0
      for j in range(len(d)):
        s += d[list(d.keys())[j]][i] * tp[j]
      if s <= 0: return 0
      prod *= s
    
    cal = 1
    for i in range(len(d[list(d.keys())[0]]) - 1, len(d[list(d.keys())[0]])):
      s = 0
      for j in range(len(d)):
        s += d[list(d.keys())[j]][i] * tp[j]
      if s <= 0: return 0
      cal *= s
    if typ == 1:
      return prod
    elif typ == 2:
      return prod if cal == 500 else 0
  else:
    a = []
    for i in range(1, 100 - sum(tp) + 1):
      a.append(rec(l, tp + [i], d, typ)) 
    return 0 if len(a) == 0 else max(a)

d = parse_input()
print('First part:', rec(len(d), [], d, 1))
print('Second part:', rec(len(d), [], d, 2))
