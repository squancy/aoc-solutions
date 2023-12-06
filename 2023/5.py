def parse_input():
  lines = open('5.txt').readlines()
  i = 0
  seeds = []
  d = {}
  while i < len(lines):
    line = lines[i].strip()
    if not line:
      i += 1
      continue
    if i == 0:
      seeds = [int(x) for x in line.replace('seeds: ', '').split(' ')]
    else:
      k, v = line.replace(' map:', '').split('-to-') 
      d[k] = {'dest': v, 'ranges': []}
      i += 1
      while i < len(lines):
        if not lines[i].strip():
          break
        d[k]['ranges'].append([int(x) for x in lines[i].split(' ')])
        i += 1
    i += 1
  return seeds, d

def first_part(seeds, d):
  locations = []
  for seed in seeds:
    cur_key = 'seed'
    t = seed
    while cur_key != 'location':
      for r in d[cur_key]['ranges']:
        if r[1] <= t <= r[1] + r[2] - 1:
          t = r[0] + t - r[1] 
          break
      cur_key = d[cur_key]['dest']
    locations.append(t)
  return min(locations)

def free_intervals(interval, sub_intervals):
  points = sorted([y for x in sub_intervals for y in x])
  points.insert(0, interval[0])
  points.append(interval[1])
  res = []
  for i in range(0, len(points) - 1, 2):
    if abs(points[i] - points[i + 1]) > 1:
      l = points[i] if i == 0 else points[i] + 1
      r = points[i + 1] if i == len(points) - 2 else points[i + 1] - 1
      res.append([l, r]) 
  return res

def rec(intervals, D, cur_key):
  if cur_key == 'location':
    return min(x[0] for x in intervals)
  ftrans = []
  for interval in intervals:
    taken_intervals = []
    transformed_intervals = [] 
    for r in D[cur_key]['ranges']:
      a, b = r[1], r[1] + r[2] - 1
      c, d = interval[0], interval[1]
      if b < c or a > d:
        continue
      else:
        e, f = max(a, c), min(b, d)
        taken_intervals.append([e, f])
        transformed_intervals.append([e + r[0] - r[1], f + r[0] - r[1]])
    transformed_intervals.extend(free_intervals(interval, taken_intervals))
    ftrans.extend(transformed_intervals)
  return rec(ftrans, D, D[cur_key]['dest'])

inp = parse_input()
print('First part:', first_part(*inp))
intervals = [[inp[0][i], inp[0][i] + inp[0][i + 1] - 1] for i in range(0, len(inp[0]), 2)]
print('Second part:', rec(intervals, inp[1], 'seed'))
