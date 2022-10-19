inp = [l.lstrip().rstrip() for l in open('inp3.txt').readlines()]
inp2 = [l.lstrip().rstrip() for l in open('inp3.txt').readlines()]
l = len(inp[0])
gamma = '0b'
epsilon = '0b'
for i in range(l):
  one = 0
  zero = 0
  for b in inp:
    if int(b[i]) == 1:
      one += 1
    else:
      zero += 1
  gamma += '1' if one > zero else '0'
  epsilon += '1' if one < zero else '0'
print('First part:', int(gamma, base=2) * int(epsilon, base=2))

def ml_common_bit(inp, typ, i):
  zero = 0
  one = 0
  for b in inp:
    if b and int(b[i]) == 1:
      one += 1
    elif b:
      zero += 1
  if typ == 'm':
    return one >= zero
  else:
    if one >= zero:
      return 0
    return 1

def only_one(inp):
  cnt = 0
  for i in range(len(inp)):
    if inp[i] != None:
      cnt += 1
      if cnt > 1:
        return False
  return True

def get_num(inp):
  for i in range(len(inp)):
    if inp[i] != None:
      return inp[i]

def get_info(inp, typ):
  pos = 0
  res = None
  while True:
    bit = ml_common_bit(inp, typ, pos)
    for i in range(len(inp)):
      if inp[i] and int(inp[i][pos]) != bit:
        inp[i] = None
    if only_one(inp):
      res = '0b' + get_num(inp)
      break
    pos += 1
  return int(res, base=2)

print('Second part:', get_info(inp, 'm') * get_info(inp2, 'l'))
