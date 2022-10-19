lines = [x for x in open('inp7.txt').readlines()]
inp = {}

for line in lines:
  s = line.split('bags contain')
  key = s[0].strip()
  v = {}
  if s[1].strip() != 'no other bags.':
    vk = s[1].split(',')
    for x in vk:
      x = x.strip()
      s2 = x.split(' ')
      v[' '.join(s2[1:-1]).strip()] = int(s2[0])
  inp[key] = v

search_for = ['shiny gold']
changed = True

while changed:
  changed = False
  for k in inp:
    for s in search_for:
      if s in inp[k]:
        if k not in search_for:
          search_for.append(k)
          changed = True
print('First part:', len(search_for) - 1) 

def shiny_bag_contains(search_for):
  if len(inp[search_for]) == 0:
    return 0
  cnt = 0
  for s in inp[search_for]:
    cnt += inp[search_for][s] + inp[search_for][s] * shiny_bag_contains(s)
  return cnt

print('Second part:', shiny_bag_contains('shiny gold'))
