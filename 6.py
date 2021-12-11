arr = [int(x) for x in open('inp6.txt').readline().split(',')]
l0 = ll0 = arr.count(0)
l1 = ll1 = arr.count(1)
l2 = ll2 = arr.count(2)
l3 = ll3 = arr.count(3)
l4 = ll4 = arr.count(4)
l5 = ll5 = arr.count(5)
l6 = ll6 = arr.count(6)
l7 = ll7 = arr.count(7)
l8 = ll8 = arr.count(8)

for k in range(80):
  ll0, ll1, ll2, ll3, ll4, ll5, ll6, ll7, ll8 = [ll1, ll2, ll3, ll4, ll5, ll6, ll7 + ll0, ll8, ll0]

for k in range(256):
  l0, l1, l2, l3, l4, l5, l6, l7, l8 = [l1, l2, l3, l4, l5, l6, l7 + l0, l8, l0]

print('First part:', ll0 + ll1 + ll2 + ll3 + ll4 + ll5 + ll6 + ll7 + ll8)
print('Second part:', l0 + l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8)
