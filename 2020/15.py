from collections import defaultdict

nums = [int(x) for x in open('inp15.txt').readline().split(',')]

def first_part(nums):
  spoken = [x for x in nums]
  for i in range(2020 - len(nums)):
    if not spoken[-1] in spoken[:-1]:
      spoken.append(0)
    else:
      li = len(spoken) - 1 - spoken[::-1].index(spoken[-1])
      li2 = len(spoken) - 1 - spoken[:li][::-1].index(spoken[-1])
      spoken.append(li - li2 + 1)
  return spoken[-1]

def second_part(nums):
  spoken = defaultdict(list)
  for i in range(len(nums)):
    spoken[nums[i]] = [i]
  last_num = nums[-1]
  cur_ind = len(spoken)
  for i in range(30000000 - len(nums)):
    if len(spoken[last_num]) >= 2:
      s = spoken[last_num]
      if len(spoken[s[-1] - s[-2]]) < 2:
        spoken[s[-1] - s[-2]].append(cur_ind)
      else:
        spoken[s[-1] - s[-2]] = [spoken[s[-1] - s[-2]][-1], cur_ind]
      last_num = s[-1] - s[-2]
    else:
      if len(spoken[0]) < 2:
        spoken[0].append(cur_ind) 
      else:
        spoken[0] = [spoken[0][-1], cur_ind]
      last_num = 0
    cur_ind += 1
  return last_num

print('First part:', first_part(nums))
print('Second part:', second_part(nums))
