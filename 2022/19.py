# 2nd part is pretty slow

blueprints = {}
for i, line in enumerate(open('19.txt').readlines()):
  bp = {}
  line = line.strip().split('.')
  for j in range(4):
    s = line[j].split(' ')
    bp[j] = [int(s[-5]), int(s[-2])] if j > 1 else [int(s[-2])]
  blueprints[i + 1] = bp

def solve(bp, resources, robots, max_geos, max_min, mxs, cache, m = 1):
  k = tuple(resources + robots)
  if (m >= max_min + 2 or (k in cache and cache[k] <= m) or 
    robots[0] > mxs[0] or robots[1] > mxs[1] or robots[2] > mxs[2]):
    return 
  
  orig_res = resources[::1]
  orig_rob = robots[::1]
  built = False
  for i in range(5):
    if i < 3:
      should_build = (max_min - m) * mxs[i] >= resources[i] + robots[i] * (max_min - m)
    if i == 3 and resources[0] >= bp[i][0] and resources[2] >= bp[i][1]:
      resources[0] -= bp[i][0]
      resources[2] -= bp[i][1]
      robots[i] += 1
      built = True
    elif i == 2 and resources[0] >= bp[i][0] and resources[1] >= bp[i][1] and should_build:
      resources[0] -= bp[i][0]
      resources[1] -= bp[i][1]
      robots[i] += 1
      built = True
    elif i == 1 and resources[0] >= bp[i][0] and should_build:
      resources[0] -= bp[i][0]
      robots[i] += 1
      built = True
    elif i == 0 and resources[0] >= bp[i][0] and should_build:
      resources[0] -= bp[i][0]
      robots[i] += 1
      built = True
    max_geos.add(resources[3])
    if i == 4 and built or i < 3 and not built: continue
    for j in range(4):
      resources[j] += orig_rob[j]
    solve(bp, resources[::1], robots[::1], max_geos, max_min, mxs, cache, m + 1)
    k = tuple(resources + robots)
    if (k in cache and m < cache[k]) or not k in cache:
      cache[k] = m 
    resources, robots = orig_res[::1], orig_rob[::1]

def get_maxes(bp):
  return [
    max(bp[i][0] for i in range(4)),
    bp[2][1],
    bp[3][1]
  ]

def first_part(blueprints):
  summa = 0
  for k in blueprints:
    cache = {}
    mxs = get_maxes(blueprints[k])
    max_geos = set()
    solve(blueprints[k], [0, 0, 0, 0], [1, 0, 0, 0], max_geos, 24, mxs, cache)
    summa += max(max_geos) * k
  return summa

def second_part(blueprints):
  prod = 1
  for k in range(1, 4):
    cache = {}
    mxs = get_maxes(blueprints[k])
    max_geos = set()
    solve(blueprints[k], [0, 0, 0, 0], [1, 0, 0, 0], max_geos, 32, mxs, cache)
    prod *= max(max_geos)
  return prod

print('First part:', first_part(blueprints))
print('Second part:', second_part(blueprints))
