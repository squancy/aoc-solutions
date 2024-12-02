f = open('1.txt').readlines()
a = sorted([int(x.split('   ')[0]) for x in f])
b = sorted([int(x.split('   ')[1]) for x in f])

def first_part():
    return sum([abs(a[i] - b[i]) for i in range(len(a))])

def second_part():
    return sum([b.count(x) * x for x in a])

print("First part:", first_part())
print("Second part:", second_part())
