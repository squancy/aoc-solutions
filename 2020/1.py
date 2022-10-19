arr = [int(x.lstrip().rstrip()) for x in open('inp1.txt').readlines()]
for i in range(len(arr) - 1):
  for j in range(i + 1, len(arr)):
    if arr[i] + arr[j] == 2020:
      print('First part:', arr[i] * arr[j])
      break

for i in range(len(arr) - 2):
  for j in range(i + 1, len(arr) - 1):
    for k in range(j + 1, len(arr)):
      if arr[i] + arr[j] + arr[k] == 2020:
        print('Second part:', arr[i] * arr[j] * arr[k])
        break

