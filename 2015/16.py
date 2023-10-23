def parse_input():
  d = {}
  for line in open('inp16.txt').readlines():
    line = line.strip()     
    p1, p2 = line.split(':')[0], ':'.join(line.split(':')[1:])
    sue_id = int(p1.replace('Sue ', ''))
    vs = {}
    for kv in p2.strip().split(','):
      k, v = kv.split(':')
      vs[k.strip()] = int(v.strip())
    d[sue_id] = vs

  info = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

  inf = {}
  for line in info.split('\n'):
    k, v = line.split(':')    
    inf[k] = int(v.strip())

  return d, inf

d, inf = parse_input()

def find_sue(d, inf):
  possible_sues = list(range(1, 501))
  for k, v in d.items():
    for ki, vi in v.items():
      if inf[ki] != v[ki]:
        possible_sues.remove(k)
        break
  return possible_sues[0]

def find_real_sue(d, inf):
  possible_sues = list(range(1, 501))
  ct = ['cats', 'trees']
  pg = ['pomeranians', 'goldfish']
  for k, v in d.items():
    for ki, vi in v.items():
      if (ki in ct and v[ki] <= inf[ki]) or (ki in pg and v[ki] >= inf[ki]) or (not ki in ct + pg and inf[ki] != v[ki]):
        possible_sues.remove(k)
        break
  return possible_sues[0]

print('First part:', find_sue(d, inf))
print('Second part:', find_real_sue(d, inf))
