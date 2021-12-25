def extract_line(line):
  typ = 0
  if line[0:2] == 'on':
    typ = 1
  line = line.replace('off ', '').replace('on ', '')
  x, y, z = [[int(x.replace('x=', '').replace('y=', '').replace('z=', '')) for x in y.split('..')] for y in line.split(',')]
  return [x, y, z, typ]

"""
def remove_invalid_ranges(ranges):
  i = 0
  while i < len(ranges):
    if ranges[i] == [None, None]:
      del ranges[i]
      i -= 1
    i += 1
  return ranges

def uncovered_range(covered, new):
  unc_r = new 
  changed = True 
  while changed:
    changed = False
    for r in covered:
      for i in range(len(unc_r)):
        ur = unc_r[i]
        if (ur[0] > r[1] and ur[1] > r[1]) or (ur[0] < r[0] and ur[1] < r[0]):
          continue
        elif ur[1] > r[1] and r[0] <= ur[0] <= r[1]:
          unc_r[i][0] = r[1] + 1
          changed = True
        elif ur[0] < r[0] and r[0] <= ur[1] <= r[1]:
          unc_r[i][1] = r[0] - 1
          changed = True
        elif r[0] <= ur[0] <= r[1] and r[0] <= ur[1] <= r[1]:
          unc_r[i] = [None, None]
          changed = True
        elif ur[0] < r[0] and ur[1] > r[1]:
          unc_r[i] = [None, None]
          unc_r.append([ur[0], r[0] - 1]) 
          unc_r.append([r[1] + 1, ur[1]]) 
          changed = True
      unc_r = remove_invalid_ranges(unc_r)
  return unc_r
        
def count_range(ranges):
  l = 0
  for r in ranges:
    l += r[1] - r[0] + 1
  return l

def count_cubes(new_vals, old_vals):
  nx, ny, nz = new_vals
  ox, oy, oz = old_vals
  return (
    nx * oy * oz +
    ny * ox * oz +
    nz * ox * oy +
    nx * ny * oz +
    nx * nz * oy +
    ny * nz * ox +
    nx * ny * nz
  )

covered_x_range = []
covered_y_range = []
covered_z_range = []
on_cubes = 0
for line in open('inp22.txt').readlines():
  line = line.lstrip().rstrip()
  x, y, z, typ = extract_line(line)
  x_save = [a for a in x]
  y_save = [a for a in y]
  z_save = [a for a in z]
  if typ == 1:
    unc_x = uncovered_range(covered_x_range, [x]) 
    unc_y = uncovered_range(covered_y_range, [y]) 
    unc_z = uncovered_range(covered_z_range, [z]) 
    
    new_x = count_range(unc_x)
    new_y = count_range(unc_y)
    new_z = count_range(unc_z)
    t1 = uncovered_range(unc_x, [x_save])
    t2 = uncovered_range(unc_y, [y_save])
    t3 = uncovered_range(unc_z, [z_save])
    old_x = count_range(t1)
    old_y = count_range(t2)
    old_z = count_range(t3)
    tmp = count_cubes([new_x, new_y, new_z], [old_x, old_y, old_z])
    on_cubes += tmp
    covered_x_range.extend(unc_x)
    covered_y_range.extend(unc_y)
    covered_z_range.extend(unc_z)
  else:
    cs = [[b for b in a] for a in covered_x_range]
    cy = [[b for b in a] for a in covered_y_range]
    cz = [[b for b in a] for a in covered_z_range]
    unc_x = uncovered_range([x], covered_x_range) 
    unc_y = uncovered_range([y], covered_y_range) 
    unc_z = uncovered_range([z], covered_z_range) 

    t1 = uncovered_range(cs, [x])
    t2 = uncovered_range(t1, [x_save])
    g1 = uncovered_range(cy, [y])
    g2 = uncovered_range(g1, [y_save])
    h1 = uncovered_range(cz, [z])
    h2 = uncovered_range(h1, [z_save])

    new_x = count_range(t2) 
    new_y = count_range(g2)
    new_z = count_range(h2)
    print(t2, g2, h2)
    on_cubes -= new_x * new_y * new_z
#print(on_cubes)
"""
"""
print(covered_x_range)
print(covered_y_range)
print(covered_z_range)
"""

x_ranges = []
y_ranges = []
z_ranges = []

for line in open('inp22.txt'):
  line = line.lstrip().rstrip()
  x, y, z, typ = extract_line(line)
  x_ranges.append(x)
  y_ranges.append(y)
  z_ranges.append(z)

x_ranges = sorted(x_ranges)
y_ranges = sorted(y_ranges)
z_ranges = sorted(z_ranges)

print(x_ranges)
print(y_ranges)
print(z_ranges)
