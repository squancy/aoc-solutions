def req1(pw):
  for i in range(len(pw) - 2):
    if ord(pw[i + 1]) - ord(pw[i]) == ord(pw[i + 2]) - ord(pw[i + 1]) == 1:
      return True
  return False

def req2(pw):
  return not ('i' in pw or 'o' in pw or 'l' in pw)

LETTERS = []
for i in range(97, 123):
  LETTERS.append(chr(i) + chr(i))

def req3(pw):
  incl = []
  for l in LETTERS:
    if l in pw:
      incl.append(l)
  return len(incl) == 2 and incl[0] != incl[1]

def increment(pw):
  pw = list(pw)
  spw = ''.join(pw)
  while not (req1(pw) and req2(pw) and req3(spw)):
    if not req2(pw):
      pos = min(spw.find('i'), spw.find('o'), spw.find('l'))
      if pos >= 0:
        pw[pos] = chr(ord(pw[pos]) + 1)
        for j in range(pos + 1, len(pw)):
          pw[j] = 'a'

    if pw[-1] == 'z':
      i = len(pw) - 1
      while True:
        if pw[i] == 'z':
          pw[i] = 'a'
        else:
          pw[i] = chr(ord(pw[i]) + 1)
          break
        i -= 1
    else:
      pw[-1] = chr(ord(pw[-1]) + 1)
    spw = ''.join(pw)
  return ''.join(pw)

print('First part:', increment('cqjxxyzz'))
print('Second part:', increment('cqjxxzaa'))
