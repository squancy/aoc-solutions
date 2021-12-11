"""
  This solution does not use brute force to determine the correct digits
"""

inp = [x for x in open('inp8.txt').readlines()]
summa = 0
signals = []
outputs = []

for l in inp:
  signals.append([x for x in l.split('|')[0].lstrip().rstrip().split(' ')])
  outputs.append([x for x in l.split('|')[1].lstrip().rstrip().split(' ')])

cnt = 0
for row in outputs:
  for el in row:
    if len(el) == 2 or len(el) == 4 or len(el) == 3 or len(el) == 7:
      cnt += 1

print('First part:', cnt)

for k in range(len(signals)):
  el = signals[k]
  arr = dict()
  sol = [None] * 10
  for seq in el:
    if len(seq) == 2:
      arr[1] = [seq]
      sol[1] = seq
    elif len(seq) == 4:
      arr[4] = [seq]
      sol[4] = seq
    elif len(seq) == 3:
      arr[7] = [seq]
      sol[7] = seq
    elif len(seq) == 7:
      arr[8] = [seq]
      sol[8] = seq
    elif len(seq) == 6:
      if 6 in arr:
        arr[6].append(seq)
      else:
        arr[6] = [seq]
    else:
      if 5 in arr:
        arr[5].append(seq)
      else:
        arr[5] = [seq]

  a = set(arr[7][0]) - set(arr[1][0])
  eg = set(arr[8][0]) - (set(arr[1][0]) | set(arr[4][0]) | set(arr[7][0]))
  cf = set(arr[1][0])
  bd = set(arr[4][0]) - set(arr[1][0])

  # determine 9
  if len(set(arr[6][0])) - len(set(arr[6][0]) - eg) == 1:
    sol[9] = arr[6][0] 
    del arr[6][0]
  elif len(set(arr[6][1])) - len(set(arr[6][1]) - eg) == 1:
    sol[9] = arr[6][1] 
    del arr[6][1]
  else:
    sol[9] = arr[6][2]
    del arr[6][2]

  # determine 6
  if len(set(arr[6][0])) - len(set(arr[6][0]) - cf) == 1:
    sol[6] = arr[6][0]
    del arr[6][0]
  else:
    sol[6] = arr[6][1]
    del arr[6][1]
  
  # determine 0
  sol[0] = arr[6][0]

  # determine 3
  if len(set(arr[5][0])) - len(set(arr[5][0]) - cf) == 2:
    sol[3] = arr[5][0]
    del arr[5][0]
  elif len(set(arr[5][1])) - len(set(arr[5][1]) - cf) == 2:
    sol[3] = arr[5][1]
    del arr[5][1]
  else:
    sol[3] = arr[5][2]
    del arr[5][2]
  
  # determine 5
  if len(set(arr[5][0])) - len(set(arr[5][0]) - bd) == 2:
    sol[5] = arr[5][0]
    del arr[5][0]
  else:
    sol[5] = arr[5][1]
    del arr[5][1]

  # determine 2
  sol[2] = arr[5][0]
  
  res = ''
  out = outputs[k]
  for cout in out:
    for i in range(len(sol)):
      if set(sol[i]) == set(cout):
        res += str(i)
        break
  summa += int(res)
print('Second part:', summa)
