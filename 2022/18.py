cubes = set([tuple([int(y) for y in x.strip().split(',')]) for x in open('18.txt').readlines()])

def connected_cubes(x, y, z):
  return set([
    (x, y, z - 1),
    (x, y, z + 1),
    (x, y - 1, z),
    (x, y + 1, z),
    (x - 1, y, z),
    (x + 1, y, z)
  ])

cache = {}

def is_air_pocket(x, y, z, cubes, max_x, max_y, max_z, visited):
  if (x, y, z) in cache:
    return cache[(x, y, z)]
  elif (x, y, z) in cubes:
    return True
  elif x > max_x or y > max_y or z > max_z:
    return False

  arr = [0 for i in range(6)]

  for i in range(1, max_x + 1):
    if (x + i, y, z) in cubes: arr[0] = 1 
    if (x - i, y, z) in cubes: arr[1] = 1
    if arr[0] == arr[1] == 1: break

  for j in range(1, max_y + 1):
    if (x, y + j, z) in cubes: arr[2] = 1 
    if (x, y - j, z) in cubes: arr[3] = 1
    if arr[2] == arr[3] == 1: break

  for k in range(1, max_z + 1):
    if (x, y, z + k) in cubes: arr[4] = 1 
    if (x, y, z - k) in cubes: arr[5] = 1
    if arr[4] == arr[5] == 1: break
  
  if not all(arr):
    cache[(x, y, z)] = False
    return False

  for cube in connected_cubes(x, y, z) - visited:
    r = is_air_pocket(*cube, cubes, max_x, max_y, max_z, visited | connected_cubes(x, y, z))
    cache[(x, y, z)] = r
    if not r:
      return False
  
  cache[(x, y, z)] = 1
  return True

def first_part(cubes):
  faces = 0
  for cube in cubes:
    faces += 6 - len(connected_cubes(*cube) & cubes)
  return faces

def second_part(cubes):
  max_x, min_x = max(x for (x, y, z) in cubes), min(x for (x, y, z) in cubes)
  max_y, min_y = max(y for (x, y, z) in cubes), min(y for (x, y, z) in cubes)
  max_z, min_z = max(z for (x, y, z) in cubes), min(z for (x, y, z) in cubes)
  air_pockets = set()
  for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
      for z in range(min_z, max_z + 1):
        if not (x, y, z) in cubes and is_air_pocket(x, y, z, cubes, max_x, max_y, max_z, set()):
          air_pockets.add((x, y, z))
  return first_part(cubes) - first_part(air_pockets)

print('First part:', first_part(cubes))
print('Second part:', second_part(cubes))
