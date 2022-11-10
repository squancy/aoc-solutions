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
  

print('First part:', first_part(cups))
