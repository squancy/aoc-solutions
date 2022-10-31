import re

rules = {}
f = open('inp19.txt')
while True:
  line = f.readline().rstrip()
  if not line: break
  s = line.split(':')
  rules[s[0]] = [x.replace('"', '') for x in s[1].split(' ') if x]

messages = [x.rstrip() for x in f.readlines()]

def expand_rule(cur_ind):
  res = '('
  for x in rules[cur_ind]:
    if x == '|':
      res += '|'
    elif not x.isnumeric():
      return f'{x}'
    else:
      res += expand_rule(x) 
  return res + ')'

def expand_rule_loop(cur_ind):
  if cur_ind == '8':
    r = expand_rule_loop('42')
    return f'{r}+'
  elif cur_ind == '11':
    res = '('
    r1 = expand_rule_loop('42')
    r2 = expand_rule_loop('31')
    for i in range(1, 50):
      res += f'({r1}{{{i}}}{r2}{{{i}}})' 
      if i < 49:
        res += '|'
    return res + ')'
  res = '('
  for x in rules[cur_ind]:
    if x == '|':
      res += '|'
    elif not x.isnumeric():
      return f'{x}'
    else:
      res += expand_rule_loop(x) 
  return res + ')'

def first_part(messages):
  p = expand_rule('0')
  cnt = 0
  for message in messages:
    if re.fullmatch(p, message):
      cnt += 1
  return cnt

def second_part(messages):
  p = expand_rule_loop('0')
  cnt = 0
  for message in messages:
    if re.fullmatch(p, message):
      cnt += 1
  return cnt

print('First part:', first_part(messages))
print('Second part:', second_part(messages))
