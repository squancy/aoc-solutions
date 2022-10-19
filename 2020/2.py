ranges = []
letters = []
passwords = []
for line in open('inp2.txt').readlines():
  line = line.lstrip().rstrip()
  ranges.append([int(line.split(' ')[0].split('-')[0]), int(line.split(' ')[0].split('-')[1])])
  letters.append(line.split(' ')[1].replace(':', ''))
  passwords.append(line.split(' ')[2])

cnt = 0
for i in range(len(passwords)):
  if ranges[i][0] <= passwords[i].count(letters[i]) <= ranges[i][1]:
    cnt += 1

print('First part:', cnt)

cnt = 0
for i in range(len(passwords)):
  if ((passwords[i][ranges[i][0] - 1] == letters[i] and passwords[i][ranges[i][1] - 1] != letters[i])
    or (passwords[i][ranges[i][0] - 1] != letters[i] and passwords[i][ranges[i][1] - 1] == letters[i])):
    cnt += 1
print('Second part:', cnt)
