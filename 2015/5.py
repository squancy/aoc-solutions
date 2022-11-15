import re

lines = [x.rstrip() for x in open('inp5.txt').readlines()]

def first_part(lines):
  cnt = 0
  for line in lines:
    p = re.compile(r'(.)\1')
    disallowed_strs = ['ab', 'cd', 'pq', 'xy']
    num_of_vowels = sum([line.count(x) for x in 'aeiou'])
    if num_of_vowels >= 3 and p.search(line) and not any([x in line for x in disallowed_strs]):
      cnt += 1
  return cnt

def second_part(lines):
  cnt = 0
  p1 = re.compile(r'.*(..).*\1.*')
  p2 = re.compile(r'(.).\1')
  for line in lines:
    if p1.search(line) and p2.search(line):
      cnt += 1
  return cnt

print('First part:', first_part(lines))
print('Second part:', second_part(lines))
