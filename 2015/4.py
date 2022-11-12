import hashlib

def find_n(num_of_zeros):
  for i in range(10 ** 7):
    if hashlib.md5(('iwrupvqb' + str(i)).encode()).hexdigest().startswith('0' * num_of_zeros):
      return i

print('First part:', find_n(5))
print('Second part:', find_n(6))
