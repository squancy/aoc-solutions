import re
from collections import defaultdict

inp = [x.rstrip() for x in open('inp14.txt').readlines()]

def mask_val(val, mask):
  b = bin(val)[2:]
  b = (36 - len(b)) * '0' + b
  res = []
  for i in range(36):
    if mask[i] == 'X':
      res.append(str(b[i]))
    else:
      res.append(str(mask[i]))
  return int(''.join(res), 2)

def first_part(inp):
  current_mask = None
  mem = defaultdict(int)
  for line in inp:
    if line.startswith('mask'):
      current_mask = line.split('=')[1].lstrip()
    else:
      p = re.compile('mem\[(\d+)\] = (\d+)')    
      mobj = p.match(line)
      addr, val = mobj.groups()
      mem[addr] = mask_val(int(val), current_mask) 

  return sum(mem.values())

def gen_all_addrs(addr):
  if not 'X' in addr:
    return [int(''.join(addr), 2)]
  v0 = [x for x in addr]
  v1 = [x for x in addr]
  ind = addr.index('X')
  v0[ind] = '0'
  v1[ind] = '1'
  return gen_all_addrs(v0) + gen_all_addrs(v1)

def decode_val(addr, mask):
  b = bin(addr)[2:]
  b = (36 - len(b)) * '0' + b
  res = []
  for i in range(36):
    if mask[i] == '1':
      res.append('1')
    elif mask[i] == '0':
      res.append(b[i])
    else:
      res.append('X')
  return gen_all_addrs(res)

def second_part(inp):
  current_mask = None
  mem = defaultdict(int)
  for line in inp:
    if line.startswith('mask'):
      current_mask = line.split('=')[1].lstrip()
    else:
      p = re.compile('mem\[(\d+)\] = (\d+)')    
      mobj = p.match(line)
      addr, val = mobj.groups()
      addrs = decode_val(int(addr), current_mask)
      for a in addrs:
        mem[a] = int(val)
  return sum(mem.values())

print('First part:', first_part(inp))
print('Second part:', second_part(inp))
