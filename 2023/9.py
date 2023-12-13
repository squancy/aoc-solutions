nums = [[int(x) for x in line.split()] for line in open('9.txt')]

def get_lf_nums(nums, last):
  lf_nums = []
  for n in nums:
    ns = [n[-1] if last else n[0]]
    cur_seq = n
    while True:
      arr = []
      all_zero = True
      for i in range(len(cur_seq) - 1):
        x = cur_seq[i + 1] - cur_seq[i]
        if (i == len(cur_seq) - 2 and last) or (i == 0 and not last):
          ns.append(x) 
        arr.append(x)
        if x != 0:
          all_zero = False
      if all_zero:
        break
      cur_seq = arr
    lf_nums.append(ns)
  return lf_nums

def first_part(nums):
  return sum(sum(get_lf_nums(nums, last = True), []))

def second_part(nums):
  res = 0
  for r in get_lf_nums(nums, last = False):
    cur_num = 0
    for x in r[::-1]:
      cur_num = x - cur_num
    res += cur_num
  return res

print('First part:', first_part(nums))
print('Second part:', second_part(nums))
