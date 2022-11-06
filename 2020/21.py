from collections import defaultdict
import re

ing = defaultdict(list)
for line in open('inp21.txt').readlines():
  line = line.rstrip()
  p = re.compile('(.+) \(contains (.+)\)') 
  obj = p.fullmatch(line)
  keys = obj.group(2).split(', ')
  v = obj.group(1).split(' ')
  for k in keys:
    ing[k].append(v) 

print(ing)
print()

def first_part(ing):
  res = []
  for k, v in ing.items():
    union = set([y for x in v for y in x])
    intersection = set(v[0])
    for i in range(1, len(v)):
      intersection &= set(v[i])
    part = list(union - intersection)

  return res

print('First part:', first_part(ing))
