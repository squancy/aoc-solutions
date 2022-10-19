def extract_line(line):
  typ = -1
  if line[0:2] == 'on':
    typ = 1
  line = line.replace('off ', '').replace('on ', '')
  x, y, z = [[int(x.replace('x=', '').replace('y=', '').replace('z=', '')) for x in y.split('..')] for y in line.split(',')]
  return [x, y, z, typ]

class Cuboid():
  def __init__(self, min_x, max_x, min_y, max_y, min_z, max_z, typ):
    self.min_x = min_x
    self.max_x = max_x
    self.min_y = min_y
    self.max_y = max_y
    self.min_z = min_z
    self.max_z = max_z
    self.typ = typ

  def intersect(self, c2):
    return (self.max_x >= c2.min_x and self.min_x <= c2.max_x and self.max_y >= c2.min_y and self.min_y <= c2.max_y and self.max_z >= c2.min_z
      and self.min_z <= c2.max_z)
  
  def intersection(self, c2):
    min_x = max(self.min_x, c2.min_x)
    max_x = min(self.max_x, c2.max_x)
    min_y = max(self.min_y, c2.min_y)
    max_y = min(self.max_y, c2.max_y)
    min_z = max(self.min_z, c2.min_z)
    max_z = min(self.max_z, c2.max_z)

    if self.typ == 1 and c2.typ == 1:
      typ = -1
    elif self.typ == 1 and c2.typ == -1:
      typ = 1
    elif self.typ == -1 and c2.typ == 1:
      typ = -1
    elif self.typ == -1 and c2.typ == -1:
      typ = 1

    return Cuboid(min_x, max_x, min_y, max_y, min_z, max_z, typ)

  def volume(self):
    return (self.max_x - self.min_x + 1) * (self.max_y - self.min_y + 1) * (self.max_z - self.min_z + 1)

def solve(t):
  vol = 0
  cuboids = []
  for line in open('inp22.txt'):
    x, y, z, typ = extract_line(line) 
    if t == 1 and (abs(x[0]) > 50 or abs(x[1]) > 50 or abs(y[0]) > 50 or abs(y[1]) > 50 or abs(z[0]) > 50 or abs(z[1]) > 50):
      continue
    cur_c = Cuboid(x[0], x[1], y[0], y[1], z[0], z[1], typ)
    intersections = []

    for c in cuboids:
      if cur_c.intersect(c):
        i = cur_c.intersection(c)
        intersections.append(i)

    for i in intersections:
      cuboids.append(i)

    if typ == 1:
      cuboids.append(cur_c)

  for c in cuboids:
    vol += c.volume() * c.typ

  return vol

print('First part:', solve(1))
print('Second part:', solve(2))
