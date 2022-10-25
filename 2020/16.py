from collections import defaultdict
import math

lines = [l.lstrip().rstrip() for l in open('inp16.txt').readlines()]
intervals = []
switch = 0
nearby_tickets = []
nearby_tickets_r = []
intd = defaultdict(list)
my_ticket = []

for line in lines:
  if not line and switch == 0:
    switch = 1
  elif not line and switch == 1:
    switch = 2
  elif not switch:
    k = line.split(':')[0]
    s = [x.lstrip().rstrip() for x in line.split(':')[1].split('or')]
    for pair in s:
      f, t = [int(x) for x in pair.split('-')]
      intervals.append([f, t])
      intd[k].append([f, t])
  elif switch == 1 and not line.startswith('your'):
    nearby_tickets_r.append([int(x) for x in line.split(',')])
    my_ticket = ([int(x) for x in line.split(',')])
  elif switch == 2 and not line.startswith('nearby'):
    nearby_tickets.extend([int(x) for x in line.split(',')])
    nearby_tickets_r.append([int(x) for x in line.split(',')])

def first_part(intervals, nearby_tickets):
  bad_tickets = []
  for ticket in nearby_tickets:
    flag = False
    for interval in intervals:
      if interval[0] <= ticket <= interval[1]:
        flag = True
        break
    if not flag:
      bad_tickets.append(ticket)
  return bad_tickets

def second_part(intervals, nearby_tickets_r, bad_tickets):
  nearby_tickets = []
  for row in nearby_tickets_r:
    gr = []
    for ticket in row:
      flag = True
      for bt in bad_tickets:
        if ticket == bt:
          flag = False
      if flag:
        gr.append(ticket)
    nearby_tickets.append(gr)

  inv = []
  mn = min([len(x) for x in nearby_tickets])

  for i in range(mn):
    x = []
    for j in range(len(nearby_tickets)):
      x.append(nearby_tickets[j][i])
    inv.append(x)
  
  dlens = []
  d = defaultdict(list)
  for k, v in intd.items():
    for f in range(len(inv)):
      if all([len(first_part(v, [inv[f][j]])) == 0 for j in range(len(inv[f]))]):
        d[k].append(f)

  for k, v in d.items():
    if k.startswith('departure'):
      dlens.append(len(v))
  
  arr = []
  for l in range(1, 20):
    for k, v in d.items():
      if len(v) == l:
        arr.append(v)

  to_remove = []
  dinds = []
  for a in arr:
    ar = [x for x in a if x not in to_remove]
    to_remove.append(ar[0])
    if len(a) in dlens:
      dinds.append(ar[0])
      dlens.remove(len(a))
      if len(dlens) == 0:
        break

  return math.prod([my_ticket[x] for x in dinds])

bad_tickets = first_part(intervals, nearby_tickets)
print('First part:', sum(bad_tickets))
print('Second part:', second_part(intd, nearby_tickets_r, bad_tickets))
