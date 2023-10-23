import itertools

conts = [int(x.strip()) for x in open('inp17.txt').readlines()]

def first_part():
  l = list(itertools.product(*[(0, 1)] * 20))
  cnt = 0
  min_conts = 100
  for seq in l:
    if sum([seq[i] * conts[i] for i in range(20)]) == 150:
      cnt += 1
      if sum(seq) < min_conts:
        min_conts = sum(seq)
  return cnt, min_conts

def second_part(min_conts):
  l = list(itertools.product(*[(0, 1)] * 20))
  cnt = 0
  for seq in l:
    if sum([seq[i] * conts[i] for i in range(20)]) == 150 and sum(seq) == min_conts:
      cnt += 1
  return cnt

ans, min_conts = first_part()
print('First part:', ans)
print('Second part:', second_part(min_conts))
