# uses fast exponentiation but still pretty slow

pk1, pk2 = [int(x.rstrip()) for x in open('inp25.txt').readlines()]

def first_part(pk1, pk2):
  P = 20201227
  k = [0, 0]
  for i in range(P):
    if pow(7, i, P) == pk1:
      k[0] = i
      break
    elif pow(7, i, P) == pk2:
      k[1] = i
      break
  if k[0] > 0:
    return pow(pk2, k[0], P)
  else:
    return pow(pk1, k[1], P)

print('First part:', first_part(pk1, pk2))
