import re

def parse_inp():
  p = re.compile('([A-Za-z]+) can fly ([0-9]+) km/s for ([0-9]+) seconds, but then must rest for ([0-9]+) seconds.')
  deers = {}
  for line in open('inp14.txt').readlines():
    line = line.rstrip()
    s = re.search(p, line)
    deers[s.group(1)] = [int(s.group(2)), int(s.group(3)), int(s.group(4))]
  return deers

def calc_dist(d, t):
  return d[0] * d[1] * (t // (d[1] + d[2])) + d[0] * min((t % (d[1] + d[2])), d[1])

def run(deers, t):
  ds = []
  for k in deers:
    d = deers[k]
    ds.append(calc_dist(d, t)) 
  return max(ds)

def empty_tbl(deers):
  return {k: 0 for k in deers}

def prun(deers):
  dist = empty_tbl(deers)
  scores = empty_tbl(deers)
  for t in range(1, 2503):
    for k in deers:
      d_dist = calc_dist(deers[k], t)
      dist[k] = d_dist
    for k in deers:
      if dist[k] == max(dist.values()):
        scores[k] += 1
  return max(scores.values())

print('First part:', run(parse_inp(), 2503))
print('Second part:', prun(parse_inp()))
