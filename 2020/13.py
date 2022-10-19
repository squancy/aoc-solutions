f = open('inp13.txt')
e_to_a = int(f.readline().rstrip())
departs = [int(x) for x in f.readline().split(',') if x != 'x']
f = open('inp13.txt')
f.readline()
all_departs = [x.rstrip() for x in f.readline().split(',')]

def first_part():
  e_bus = None
  sdiff = None
  for d in departs:
    if e_to_a % d == 0:
      e_bus = d
      sdiff = 0
      break
    diff = ((e_to_a // d) * d + d) - e_to_a
    if sdiff == None or diff < sdiff:
      sdiff = diff
      e_bus = d
  return e_bus * sdiff

def chrem(congruence1, congruence2):
  (a1, n1) = congruence1
  (a2, n2) = congruence2

  (moduloGcd, u, v) = extended_gcd(n1, n2)

  if moduloGcd == 1:
    solution = n1 * a2 * u + n2 * a1 * v
    modulo = n1 * n2
    return (solution % modulo, modulo)

  if (a1 - a2) % moduloGcd != 0:
    return None

  moduloLcm = (n1 // moduloGcd) * n2
  k = (a1 - a2) // moduloGcd
  solution = a1 - n1 * u * k

  return (solution % moduloLcm, moduloLcm)

def gcd(a, b):
  while True:
    if b == 0:
      return a
    a = a % b
    if a == 0:
      return b
    b = b % a

def extended_gcd(a, b):
  if a == 0:
    return (b, 0, 1)

  if b == 0:
    return (a, 1, 0)

  unPrev = 1
  vnPrev = 0
  unCur = 0
  vnCur = 1

  while True:
    qn = a // b
    newR = a % b
    a = b
    b = newR

    if b == 0:
      return (a, unCur, vnCur)

    # Update coefficients
    unNew = unPrev - qn * unCur
    vnNew = vnPrev - qn * vnCur

    # Shift coefficients
    unPrev = unCur
    vnPrev = vnCur
    unCur = unNew
    vnCur = vnNew
    
def chrem_multiple(congruences):
  if len(congruences) == 0:
    return None
  if len(congruences) == 1:
    return congruences[0]

  solution = chrem(congruences[0], congruences[1])

  if solution == None:
    return None

  for congruence in congruences[2::]:
    solution = chrem(solution, congruence)

    if solution == None:
      return None

  return solution

def second_part():
  N = 367
  ind = all_departs.index(str(N))  
  congruences = [(0, N)]
  for i in range(1, ind + 1):
    if all_departs[ind - i] != 'x':
      congruences.append((i, int(all_departs[ind - i]))) 
  for i in range(1, len(all_departs) - ind):
    if all_departs[ind + i] != 'x':
      congruences.append((-i, int(all_departs[ind + i])))
  return chrem_multiple(congruences)[0] - ind

print('First part:', first_part())
print('Second part:', second_part())
