inp = [int(x) for x in open('inp1.txt').readlines()]

inp_three = []
for i in range(len(inp) - 2):
  inp_three.append(inp[i] + inp[i + 1] + inp[i + 2])

def count_inc(inp):
  cnt = 0
  for i in range(2, len(inp)):
    if inp[i] > inp[i - 1]:
      cnt += 1
  return cnt

print('First part:', count_inc(inp))
print('Second part:', count_inc(inp_three))

