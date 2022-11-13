cups = [int(x) for x in list(open('inp23.txt').readline().rstrip())]

def three_cups(cups, current_cup):
  ind = cups.index(current_cup)
  if ind < len(cups) - 3:
    return cups[ind + 1:ind + 4]
  elif ind == len(cups) - 3:
    return cups[ind + 1:ind + 3] + [cups[0]]
  elif ind == len(cups) - 2:
    return cups[ind + 1:ind + 2] + [cups[0], cups[1]]
  elif ind == len(cups) - 1:
    return [cups[0], cups[1], cups[2]]

def first_part(cups):
  current_cup = cups[0]
  minval = min(cups)
  maxval = max(cups)
  for i in range(100):
    tcups = three_cups(cups, current_cup) 
    destination_cup = current_cup - 1
    while not destination_cup in cups or destination_cup in tcups:
      destination_cup -= 1
      if destination_cup < minval:
        destination_cup = maxval 
    cups = [x for x in cups if not x in tcups]
    dind = cups.index(destination_cup) 
    cups = cups[:dind + 1] + tcups + cups[dind + 1:]
    cind = cups.index(current_cup)
    current_cup = cups[cind + 1] if cind + 1 < len(cups) else cups[0]
  oneind = cups.index(1)
  return ''.join([str(x) for x in cups[oneind + 1:] + cups[:oneind]])

def second_part(cups):
  d = {}
  for i in range(len(cups)):
    if i < len(cups) - 1:
      d[cups[i]] = cups[i + 1]
    else:
      d[cups[i]] = max(cups) + 1
  
  for i in range(max(cups) + 1, 10 ** 6 + 1):
    if i == 10 ** 6:
      d[i] = cups[0]
    else:
      d[i] = i + 1

  ccup = cups[0]
  minval = min(d.keys())
  maxval = max(d.keys())
  for i in range(10 ** 7):
    tcups = [d[ccup], d[d[ccup]], d[d[d[ccup]]]]
    dcup = ccup - 1 
    while not dcup in d or dcup in tcups:
      dcup -= 1
      if dcup < minval:
        dcup = maxval 
    old_nb = d[dcup]
    onb = d[tcups[2]]
    d[dcup] = tcups[0]
    d[tcups[2]] = old_nb
    d[ccup] = onb
    ccup = d[ccup]
  return d[1] * d[d[1]]

print('First part:', first_part(cups))
print('Second part:', second_part(cups))
