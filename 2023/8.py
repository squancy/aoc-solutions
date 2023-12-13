from math import gcd

def lcm(lst):
  res = 1
  for i in lst:
    res = res * i // gcd(res, i)
  return res

def parse_input():
  lines = [x.strip() for x in open('8.txt').readlines()]
  instr = None
  d = {} 
  for i in range(len(lines)):
    if i == 0:
      instr = lines[i].replace('L', '0').replace('R', '1')
    elif not lines[i]:
      continue
    else:
      l, r = lines[i].split(' = ')  
      d[l] = r.replace('(', '').replace(')', '').split(', ')
  return instr, d

def first_part(instr, d):
  cur_node = 'AAA'
  instr_pos = 0
  steps = 0
  while cur_node != 'ZZZ':
    cur_node = d[cur_node][int(instr[instr_pos])]  
    steps += 1
    instr_pos = (instr_pos + 1) % len(instr)
  return steps

# May only give the corrent answer for my input; TODO: fix later
def second_part(instr, d):
  endA = [x for x in d if x[2] == 'A']
  endZ = {x: 1 for x in d if x[2] == 'Z'}
  X = {}
  Y = {}
  for cur_node in endA:
    instr_pos = 0
    steps = 0
    orig = cur_node
    X = {}
    Y[orig] = []
    while True:
      cur_node = d[cur_node][int(instr[instr_pos])]  
      steps += 1
      instr_pos = (instr_pos + 1) % len(instr)
      if cur_node in endZ:
        Y[orig] = steps
        steps = 0
        if (cur_node, instr_pos) in X:
          break
      X[(cur_node, instr_pos)] = 1
  return lcm(list(Y.values()))

inp = parse_input()
print('First part:', first_part(*inp))
print('Second part:', second_part(*inp))
