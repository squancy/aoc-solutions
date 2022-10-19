lines = [l.lstrip().rstrip() for l in open('inp16.txt').readlines()]
intervals = []
switch = 0
my_ticket = []
nearby_tickets = []

for line in lines:
  if not line and switch == 0:
    switch = 1
  elif not line and switch == 1:
    switch = 2
  elif not switch:
    s = [x.lstrip().rstrip() for x in line.split(':')[1].split('or')]
    for pair in s:
      f, t = [int(x) for x in pair.split('-')]
      intervals.append([f, t])
  elif switch == 1 and not line.startswith('your'):
    my_ticket = [int(x) for x in line.split(',')] 
  elif switch == 2 and not line.startswith('nearby'):
    nearby_tickets.extend([int(x) for x in line.split(',')])

def first_part(intervals, nearby_tickets):
  summa = 0
  for ticket in nearby_tickets:
    flag = False
    for interval in intervals:
      if interval[0] <= ticket <= interval[1]:
        flag = True
        break
    if not flag:
      summa += ticket
  return summa

def second_part(intervals, nearby_tickets):
  pass

print('First part:', first_part(intervals, nearby_tickets))
