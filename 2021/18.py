import math

"""
  Second part could be optimized, currently takes ~15-20 secs to run
  Solved it without converting the array into a tree
"""

inp = [y.lstrip().rstrip() for y in open('inp18.txt').readlines()]
nums = []
for num in inp:
  nums.append(eval(num)) 

def get_int(arr, path):
  if type(arr) is int:
    return arr
  else:
    p = path[0]
    rest = path[1:]
    return get_int(arr[p], rest)

def has_split(arr, fix_arr, path):
  if type(arr) is int and arr >= 10:
    el = get_int(fix_arr, path)
    return (True, path, [math.floor(el / 2), math.ceil(el / 2)])
  elif type(arr) is int:
    return (False, [])
  else:
    p0 = [x for x in path] + [0]
    p1 = [x for x in path] + [1]
    v0 = has_split(arr[0], fix_arr, p0)
    v1 = has_split(arr[1], fix_arr, p1)
    if v0[0]: return v0
    if v1[0]: return v1
    return (False, [])

def has_explode(arr, path, cnt):
  if cnt == 4 and type(arr) is list and len(arr) == 2 and type(arr[0]) is int and type(arr[1]) is int:
    return (True, path)
  elif type(arr) is int:
    return (False, [])
  else:
    p0 = [x for x in path] + [0]
    p1 = [x for x in path] + [1]
    v0 = has_explode(arr[0], p0, cnt + 1)
    v1 = has_explode(arr[1], p1, cnt + 1)
    if v0[0]: return v0
    if v1[0]: return v1
    return (False, [])

def build_arr(arr, path, cur_path, repl):
  if path == cur_path:
    return repl
  elif type(arr) is int:
    return arr
  else:
    p0 = [x for x in cur_path] + [0]
    p1 = [x for x in cur_path] + [1]
    return [build_arr(arr[0], path, p0, repl)] + [build_arr(arr[1], path, p1, repl)]

def find_path(arr, path, typ):
  if typ == 'left':
    o = 1
    z = 0
  else:
    o = 0
    z = 1

  ind = None
  for i in range(len(path) - 1, -1, -1):
    if path[i] == o:
      ind = i
      break
  if ind == None:
    return (False, [])
  path = [path[i] for i in range(len(path)) if i < ind] + [z]
  for d in path:
    arr = arr[d]
  while type(arr) is not int:
    arr = arr[o]
    path.append(o)
  return (True, path)

def reduce_arr(arr):
  hp = [True]
  he = [True]
  while hp[0] or he[0]:
    hp = has_split(arr, arr, [])
    he = has_explode(arr, [], 0)
    if he[0]:
      left_val = get_int(arr, he[1] + [0]) 
      right_val = get_int(arr, he[1] + [1])
      arr = build_arr(arr, he[1], [], 0)      
      left_path = find_path(arr, he[1], 'left')
      right_path = find_path(arr, he[1], 'right')
      if left_path[0]:
        v = left_val + get_int(arr, left_path[1]) 
        arr = build_arr(arr, left_path[1], [], v)
      if right_path[0]:
        v = right_val + get_int(arr, right_path[1]) 
        arr = build_arr(arr, right_path[1], [], v)
    elif hp[0]:
      arr = build_arr(arr, hp[1], [], hp[2])
  return arr

def magnitude(arr):
  if type(arr) is int:
    return arr
  else:
    return 3 * magnitude(arr[0]) + 2 * magnitude(arr[1])

arr = nums[0]
for i in range(1, len(nums)):
  arr = reduce_arr([arr] + [nums[i]])
print('First part:', magnitude(arr))

largest = None
cnt = 0
for i in range(len(nums)):
  for j in range(len(nums)):
    if i == j: continue
    v = magnitude(reduce_arr([nums[i]] + [nums[j]])) 
    if largest == None or v > largest:
      largest = v
    cnt += 1
print('Second part:', largest)
