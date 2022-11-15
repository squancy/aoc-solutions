from collections import defaultdict

lines = [x.rstrip() for x in open('inp6.txt').readlines()]
instr = []
for line in lines:
  if line.startswith('turn on'):
    typ = 1
  elif line.startswith('turn off'):
    typ = 2
  else:
    typ = 3
  instr.append([typ, [[int(x) for x in y.split(',')] for y in line.replace('turn off ', '').replace('turn on ', '').replace('toggle ', '').split(' through ')]])

def first_part(instr):
  turned_on = {}
  for ins in instr:
    if ins[0] == 1:
      for i in range(ins[1][0][0], ins[1][1][0] + 1):
        for j in range(ins[1][0][1], ins[1][1][1] + 1):
          turned_on[(i, j)] = 1
    elif ins[0] == 2:
      for i in range(ins[1][0][0], ins[1][1][0] + 1):
        for j in range(ins[1][0][1], ins[1][1][1] + 1):
          if (i, j) in turned_on: del turned_on[(i, j)]
    else:
      for i in range(ins[1][0][0], ins[1][1][0] + 1):
        for j in range(ins[1][0][1], ins[1][1][1] + 1):
          if not (i, j) in turned_on: turned_on[(i, j)] = 1
          else: del turned_on[(i, j)]
  return len(turned_on)

def second_part(instr):
  turned_on = {}
  for ins in instr:
    if ins[0] == 1:
      for i in range(ins[1][0][0], ins[1][1][0] + 1):
        for j in range(ins[1][0][1], ins[1][1][1] + 1):
          if (i, j) in turned_on: turned_on[(i, j)] += 1
          else: turned_on[(i, j)] = 1
    elif ins[0] == 2:
      for i in range(ins[1][0][0], ins[1][1][0] + 1):
        for j in range(ins[1][0][1], ins[1][1][1] + 1):
          if (i, j) in turned_on and turned_on[(i, j)] > 0: turned_on[(i, j)] -= 1
    else:
      for i in range(ins[1][0][0], ins[1][1][0] + 1):
        for j in range(ins[1][0][1], ins[1][1][1] + 1):
          if (i, j) in turned_on: turned_on[(i, j)] += 2
          else: turned_on[(i, j)] = 2
  return sum(turned_on.values())

print('First part:', first_part(instr))
print('Second part:', second_part(instr))
