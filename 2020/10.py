jolts = [int(x) for x in open('inp10.txt').readlines()]
max_jolt = max(jolts) + 3
jolts.append(max_jolt)

def find_connection(current_jolt, jolts, diffs = [0, 0, 0]):
  js = [current_jolt + 1, current_jolt + 2, current_jolt + 3]
  for i in range(3):
    if js[i] in jolts:
      diffs[i] += 1
      find_connection(js[i], jolts, diffs)
      break
  
  return diffs[0] * diffs[2]
    
print('First part:', find_connection(0, jolts))

def all_connections(jolts):
  res = {}
  for j in jolts:
    res[j] = 0
  res[jolts[-1]] = 1
  
  for i in range(len(jolts) - 2, -1, -1):
    for j in range(1, 4):
      res[jolts[i]] += 0 if not jolts[i] + j in jolts else res[jolts[i] + j]

  return res[0]

jolts.append(0)
print('Second part:', all_connections(sorted(jolts)))
