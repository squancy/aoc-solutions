arr = []
inp = [x.rstrip() for x in open('1.txt').readlines()]
subarr = []
for i in range(len(inp)):
  if not inp[i] or i == len(inp) - 1:
    arr.append(subarr)
    subarr = []
  else:
    subarr.append(int(inp[i]))

arr = sorted([sum(x) for x in arr], reverse=True)

print('First part:', arr[0])
print('Second part:', sum(arr[:3]))
