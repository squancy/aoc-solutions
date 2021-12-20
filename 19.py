"""
  I could not come up with an efficient solution to the first part so it runs in ~8 mins  
  For the 2nd part the array of any 2 scanner is built without using any external libraries
"""

scanners = []
tmp = []
f = open('inp19.txt').readlines()
for i in range(len(f)):
  l = f[i]
  l = l.lstrip().rstrip()
  if l[0:3] == '---':
    tmp = []
  elif l:
    tmp.append([int(x) for x in l.split(',')])
  if not l or i == len(f) - 1:
    scanners.append(tmp) 

def get_rot(n, pos):
  x, y, z = pos[0], pos[1], pos[2]
  rot = {
    1: [x,y,z],
    2: [x,-y,-z],
    3: [-x,y,-z],
    4: [-x,-y,z],
    5: [x,z,-y],
    6: [x,-z,y],
    7: [-x,z,y],
    8: [-x,-z,-y],
    9: [y,z,x],
    10: [y,-z,-x],
    11: [-y,z,-x],
    12: [-y,-z,x],
    13: [y,x,-z],
    14: [y,-x,z],
    15: [-y,x,z],
    16: [-y,-x,-z],
    17: [z,x,y],
    18: [z,-x,-y],
    19: [-z,x,-y],
    20: [-z,-x,y],
    21: [z,y,-x],
    22: [z,-y,x],
    23: [-z,y,x],
    0: [-z,-y,-x]
  }
  return rot[n]

def gen_all_rots(sj):
  all_rots = []
  tmp = []
  for n in range(24):
    for i in range(len(sj)):
      p = get_rot(n, sj[i])
      tmp.append(p)
    all_rots.append(tmp)
    tmp = []
  return all_rots

all_scans = 0
for sc in scanners:
  for r in sc:
    all_scans += 1

matched = [scanners[0]]
unmatched = scanners[1:]
i = 0

scanner_pos = []

while len(matched) < len(scanners):
  si = matched[i]
  j = 0
  while j < len(unmatched):
    sj = unmatched[j]
    if sj == None:
      j += 1
      continue
    all_rots = gen_all_rots(sj)
    flag = None
    for k in range(len(all_rots)):
      for ark in all_rots[k]:
        for sil in si:
          pot_pos = [sil[0] - ark[0], sil[1] - ark[1], sil[2] - ark[2]]
          bc = 0
          flag = False
          for el in all_rots[k]:
            if [el[0] + pot_pos[0], el[1] + pot_pos[1], el[2] + pot_pos[2]] in si:
              bc += 1
          if bc == 12 and not flag:
            scanner_pos.append(pot_pos)
            flag = True
            na = []
            for e in all_rots[k]:
              x = [e[0] + pot_pos[0], e[1] + pot_pos[1], e[2] + pot_pos[2]]
              na.append(x)
            matched.append(na)
            unmatched[j] = None
            print(scanner_pos)
            break
        if flag:
          break
    j += 1
  i += 1

bc = []
for a in matched:
  for b in a:
    if not b in bc: 
      bc.append(b)
print('First part:', len(bc))

pos_combs = []

for i in range(len(scanner_pos) - 1):
  for j in range(i + 1, len(scanner_pos)):
    pos_combs.append([scanner_pos[i], scanner_pos[j]]) 

largest = None
for pair in pos_combs:
  d = abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1]) + abs(pair[0][2] - pair[1][2])
  if largest == None or d > largest:
    largest = d
print('Second part', largest)
