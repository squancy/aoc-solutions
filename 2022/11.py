import re, math, copy
from collections import defaultdict

monkeys = {}
cur_monkey = None
cur_dict = {}
f = open('11.txt').readlines()
for i in range(len(f)):
  line = f[i].strip()
  if line.startswith('Monkey'):
    cur_monkey = int(line.split(' ')[1].replace(':', ''))
  elif line.startswith('Starting'):
    cur_dict['items'] = [int(x) for x in line.split(':')[1].split(',')] 
  elif line.startswith('Operation'):
    p = re.compile(r'old (\+|\*) (old|\d+)')
    m = re.match(p, line.split('=')[1].strip())
    cur_dict['op'] = [m.groups()[0], m.groups()[1]]
  elif line.startswith('Test'):
    cur_dict['test'] = int(line.split('by')[1].strip())
  elif line.startswith('If true'):
    cur_dict['true'] = int(line.split('monkey')[1].strip())
  elif line.startswith('If false'):
    cur_dict['false'] = int(line.split('monkey')[1].strip())
  if not line or i == len(f) - 1:
    monkeys[cur_monkey] = cur_dict
    cur_dict = {}

num_of_monkeys = cur_monkey + 1
ms = copy.deepcopy(monkeys)

def apply_op(worry_level, op, v):
  ot = worry_level if v == 'old' else int(v)
  return worry_level + ot if op == '+' else worry_level * ot

def solve(monkeys, num_of_monkeys, div, rounds):
  num_of_insp = defaultdict(int)
  mod_prod = math.prod(monkeys[i]['test'] for i in range(num_of_monkeys))
  for r in range(rounds):
    for i in range(num_of_monkeys):
      for item in monkeys[i]['items']:
        num_of_insp[i] += 1
        ao = apply_op(item, *monkeys[i]['op']) // div
        if ao % monkeys[i]['test'] == 0:
          monkeys[monkeys[i]['true']]['items'].append(ao)
        else:
          monkeys[monkeys[i]['false']]['items'].append(ao)
      monkeys[i]['items'] = []
    for j in range(num_of_monkeys):
      monkeys[j]['items'] = [x % mod_prod for x in monkeys[j]['items']]

  return math.prod(sorted(num_of_insp.values(), reverse = True)[:2])

print('First part:', solve(monkeys, num_of_monkeys, 3, 20))
print('Second part:', solve(ms, num_of_monkeys, 1, 10 ** 4))
