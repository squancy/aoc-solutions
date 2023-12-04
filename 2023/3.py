def is_special(c):
  return c != '.' and not c.isdigit()

def check(start_pos, end_pos, j, inp):
  for i in range(max(0, start_pos - 1), min(end_pos + 1, len(inp[0]))):
    try:
      if is_special(inp[j][i]):
        return True
    except IndexError:
      pass
  return False

def is_symbol_around_num(start_pos, end_pos, j, inp):
  x1 = check(start_pos, end_pos, j - 1, inp) 
  x2 = check(start_pos, end_pos, j + 1, inp)
  x3 = start_pos > 0 and is_special(inp[j][start_pos - 1])
  x4 = end_pos < len(inp[0]) - 1 and is_special(inp[j][end_pos])
  return any((x1, x2, x3, x4))

def get_nums(inp):
  res = dict()
  for j in range(len(inp)):
    res[j] = []
    line = inp[j]
    i = 0
    while i < len(line):
      flag = True
      start_pos = i
      while i < len(line) and line[i].isdigit():
        flag = False
        i += 1
      if flag:
        i += 1
      else:
        res[j].append([start_pos, i])
    j += 1
  return res

def first_part(nums, inp):
  res = 0
  for k, v in nums.items():
    for start_pos, end_pos in v:
      if is_symbol_around_num(start_pos, end_pos, k, inp):
        res += int(inp[k][start_pos:end_pos])
  return res

def get_nbs(gp):
  nbs = []
  for i in range(gp[0] - 1, gp[0] + 2):
    for j in range(gp[1] - 1, gp[1] + 2):
      if (i, j) != gp: nbs.append((i, j))
  return nbs

def second_part(nums, inp):
  res = 0
  gear_pos = [(i, j) for i in range(len(inp)) for j in range(len(inp[i])) if inp[i][j] == '*'] 
  for gp in gear_pos:
    nums_around = dict()
    for nb in get_nbs(gp):
      if nb[0] in nums:
        for sp, ep in nums[nb[0]]:
          if sp <= nb[1] < ep:
            nums_around[(sp, ep, nb[0])] = 1
    if len(nums_around.keys()) == 2:
      prod = 1
      for k in nums_around:
        prod *= int(inp[k[2]][k[0]:k[1]])
      res += prod
  return res

inp = [line.strip() for line in open('3.txt').readlines()]
nums = get_nums(inp)
print('First part:', first_part(nums, inp))
print('Second part:', second_part(nums, inp))
