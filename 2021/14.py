s = open('inp14.txt').readline().lstrip().rstrip()
rules = {x.split('->')[0].rstrip().rstrip(): x.split('->')[1].lstrip().rstrip() for x in open('inp14.txt').readlines() if '->' in x}

"""
  First part is really inefficient above step 16-17
  Second solution only keeps track of the number of letters and polymer pairs, usable up to several
  thousands of steps
"""

def elements_init():
  elements = dict()
  for c in s:
    if c in elements:
      elements[c] += 1
    else:
      elements[c] = 1
  return elements

elements = elements_init()

s_save = s

for i in range(10):
  j = 0
  new_s = ''
  while j < len(s):
    if j < len(s) - 1:
      k = s[j] + s[j + 1]
      if k in rules.keys():
        new_s += s[j] + rules[k]
        if rules[k] in elements:
          elements[rules[k]] += 1
        else:
          elements[rules[k]] = 1
      else:
        new_s += s[j]
    else:
      new_s += s[j]
    j += 1
  s = new_s

so = list(sorted(elements.items(), key=lambda item: item[1]))
print('First part:', so[-1][1] - so[0][1])

s = s_save
elements = elements_init()

pairs = {}
for rule in rules:
  pairs[rule] = s.count(rule)

def dict_add(d, el, m):
  if el in d:
    d[el] += m
  else:
    d[el] = 1

for i in range(40):
  pairs_to_add = []
  for pair in pairs:
    if pairs[pair] > 0:
      new_char = rules[pair]
      dict_add(elements, new_char, pairs[pair])
      new_pair1 = pair[0] + new_char
      new_pair2 = new_char + pair[1]
      if new_pair1 in rules:
        pairs_to_add.append([new_pair1, pairs[pair]])
      if new_pair2 in rules:
        pairs_to_add.append([new_pair2, pairs[pair]])
      pairs[pair] = 0
  for pair in pairs_to_add:
    dict_add(pairs, pair[0], pair[1])

so = list(sorted(elements.items(), key=lambda item: item[1]))
print('Second part:', so[-1][1] - so[0][1])
