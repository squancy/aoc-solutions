inp = [list(x.rstrip()) for x in open('inp11.txt').readlines()]

def pretty_print(arr):
  for line in arr:
    print(''.join(line))

def access(i, j, arr):
  try:
    x = arr[i][j]
    return x
  except IndexError:
    return False

def no_occupied_seats(i, j, arr):
  pos = [-1, 0, 1]
  for p1 in pos:
    for p2 in pos:
      if p1 == p2 == 0:
        continue
      if i + p1 >= 0 and j + p2 >= 0 and access(i + p1, j + p2, arr) == '#':
        return False
  return True

def noc_dir(i, j, arr):
  pos = [-1, 0, 1]
  for p1 in pos:
    for p2 in pos:
      ic = i
      jc = j 
      if p1 == p2 == 0:
        continue 
      while True:
        ic += p1
        jc += p2
        if not len(inp) > ic >= 0 or not len(inp[0]) > jc >= 0 or arr[ic][jc] == 'L':
          break
        elif arr[ic][jc] == '#':
          return False
  return True

def four_occ_seats(i, j, arr):
  pos = [-1, 0, 1]
  cnt = 0
  for p1 in pos:
    for p2 in pos:
      if p1 == p2 == 0:
        continue
      if i + p1 >= 0 and j + p2 >= 0 and access(i + p1, j + p2, arr) == '#':
        cnt += 1
        if cnt >= 4:
          return True
  return False

def five_occ_seats(i, j, arr):
  pos = [-1, 0, 1]
  cnt = 0
  for p1 in pos:
    for p2 in pos:
      ic = i
      jc = j
      if p1 == p2 == 0:
        continue 
      while True:
        ic += p1
        jc += p2
        if not len(inp) > ic >= 0 or not len(inp[0]) > jc >= 0 or arr[ic][jc] == 'L':
          break
        elif arr[ic][jc] == '#':
          cnt += 1
          if cnt >= 5:
            return True
          break
  return False

def count_occ_seats(inp):
  cnt = 0
  for line in inp:
    for ch in line:
      if ch == '#':
        cnt += 1
  return cnt

def solve(inp, funcs):
  changed = True
  while changed:
    nx = [[y for y in x] for x in inp]
    changed = False
    for i in range(len(inp)):
      for j in range(len(inp[i])):
        ch = inp[i][j]
        if ch == 'L' and funcs[0](i, j, inp):
          nx[i][j] = '#'
          changed = True
        elif ch == '#' and funcs[1](i, j, inp):
          nx[i][j] = 'L'
          changed = True
    inp = nx
  return count_occ_seats(inp)

print('First part:', solve(inp, [no_occupied_seats, four_occ_seats]))
print('Second part:', solve(inp, [noc_dir, five_occ_seats]))
