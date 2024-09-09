import itertools
import math

nums = [int(x) for x in open('23.txt').readlines()]
sm3 = sum(nums) // 3
sm4 = sum(nums) // 4

def first_part(sm, nums):
    prod = float('inf')
    for i in range(1, len(nums)):
        combs = itertools.combinations(nums, i)
        found = False
        for comb in combs:
            if sum(comb) == sm:
                found = True
                p = math.prod(comb)
                if p < prod:
                    prod = p
        if found:
            break
    return prod

print('First part:', first_part(sm3, nums))
print('First part:', first_part(sm4, nums))
