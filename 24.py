import re, sys

"""
The assembly program can be separated into 14 parts with identical structure but different
constant values
Each part reads a number between 1 and 9 into w and then performs some operation
x and y will be overwritten in every part but z propagates through the entire program
The structure of a single part translated into pseudocode is the following:
  x = z % 26 + [constant]
  z //= [1 or 26]
  x = 1 if x == w else x = 0
  x = !x
  z *= 25 * x + 1
  y = (w + [constant]) * x
  z += y

Each part floor divides z by 26 or 1, then optionally multiplies z by 26 and then adds a
constant value (part of which is w)
In order for the last part to return 0 the input to that part must be less than 26 so that
when floor dividing z by 26 its value will be 0 (x will also need to be 0 so that no constant
is added to z)

x can only be zero at the end of a part if it's equal to w at the beginning
But x is z mod 26 so its value is always between 0 and 25 before testing its value against w 

There are 6 parts when it's possible that x == w (when a negative number is added to x) so each
part must have x == w in order to have an input for the last part that is less than 26

Given these, each part can be translated into the following equations:
  1. z = 11..19
  2. z = 26z + w + 5
  3. z = 26z + w + 12 -> mod 26 is w + 12
  4. z % 26 should be 13..21
  ...
  14. z % 26 should be 14..22

These constraints significantly reduce the number of possible options for a valid model number
With a little trial and error now it's possible to reverse engineer the largest and smallest model numbers
since there are ~ 30 million potential cases
"""

def is_num(n):
  res = re.match("[-+]?\d+$", n)
  return res is not None

def execute_instruction(instruction, w, x, y, z):
  var_lookup = {
    'w': 0,
    'x': 1,
    'y': 2,
    'z': 3
  }

  variables = [w, x, y, z]

  fields = instruction.split(' ')
  operator = fields[0]
  operand1 = fields[1]
  operand2 = fields[2]
  ind1 = var_lookup.get(operand1)
  ind2 = var_lookup.get(operand2)
  if operator == 'add':
    variables[ind1] += int(operand2) if is_num(operand2) else variables[ind2]
  elif operator == 'mul':
    variables[ind1] *= int(operand2) if is_num(operand2) else variables[ind2]
  elif operator == 'div':
    variables[ind1] //= int(operand2) if is_num(operand2) else variables[ind2]
  elif operator == 'mod':
    variables[ind1] %= int(operand2) if is_num(operand2) else variables[ind2]
  elif operator == 'eql':
    variables[ind1] = 1 if variables[ind1] == (int(operand2) if is_num(operand2) else variables[ind2]) else 0
  return variables
    

instructions = []
tmp = []
f = open('inp24.txt').readlines()
for i in range(len(f)):
  line = f[i].rstrip().lstrip()
  if (line[0:3] == 'inp' and i != 0) or i == len(f) - 1:
    if i == len(f) - 1:
      tmp.append(line)
    instructions.append(tmp)
    tmp = []
  elif line[0:3] != 'inp':
    tmp.append(line)


def run(ws):
  x, y, z = 0, 0, 0
  for i in range(len(ws)):
    w = ws[i]
    part = instructions[i]
    for instruction in part:
      w, x, y, z = execute_instruction(instruction, w, x, y, z)
  return z


init = [9,9,9,9,5,9,6,9,9,1,9]
for d1 in range(9, 0, -1):
  for d2 in range(9, 0, -1):
    for d3 in range(9, 0, -1):
      ws = init + [d1, d2, d3]
      res = run(ws)
      if res == 0:
        print('First part:', ''.join([str(x) for x in ws]))

init = [1, 1, 1, 1, 1, 5, 1, 4, 1, 1, 9]
for ds1 in range(1, 10):
  for ds2 in range(1, 10):
    for d1 in range(1, 10):
      for d2 in range(1, 5):
        for d3 in range(1, 6):
          for d4 in range(1, 10):
            for d5 in range(1, 10):
              for d6 in range(1, 10):
                ws = [ds1, ds2]
                ws.append(d1)
                ws.append(d1)
                ws.append(d2)
                ws.append(d2 + 6 - 2)
                ws.append(d3)
                ws.append(d3 + 15 - 12)
                ws.append(d4)
                ws.append(1)
                ws.append(9)
                ws.append(d5)
                ws.append(d6)
                ws.append(1)
                res = run(ws)
                if res == 0:
                  print('Second part:', ''.join([str(x) for x in ws]))
                  sys.exit()
