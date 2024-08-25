import math

def divs(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        yield divisor

def first_part():
    n = 1
    while True:
        p = sum(list(divs(n))) * 10
        if p >= 29000000:
            return n
        n += 1

def second_part():
    n = 1
    while True:
        p = sum([x for x in list(divs(n)) if x >= n // 50]) * 11
        if p >= 29000000:
            return n
        n += 1
print(second_part())

