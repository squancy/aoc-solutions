inp = [int(x.rstrip()) for x in open('inp9.txt').readlines()]

ans = None
for i in range(25, len(inp)):
  found = False
  for j in range(i - 25, i):
    for k in range(j + 1, i):
      if inp[j] + inp[k] == inp[i]:
        found = True
        break
    if found:
      break
  if not found:
    ans = inp[i]
    print('First part:', inp[i])
    break

for i in range(len(inp)):
  arr = [inp[i]]
  summa = inp[i]
  for j in range(i + 1, len(inp)):
    summa += inp[j]
    arr.append(inp[j])
    if summa == ans:
      print('Second part:', min(arr) + max(arr))
    elif summa > ans:
      break
