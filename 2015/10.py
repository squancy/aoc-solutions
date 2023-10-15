seq = open('inp10.txt').readline().rstrip()

def get_blocks(seq):
  blocks = []
  cur_block = []
  for i in range(len(seq)):
    cur_block.append(seq[i]) 
    if i == len(seq) - 1 or seq[i] != seq[i + 1]:
      blocks.append(cur_block)
      cur_block = []
  return blocks

def look_and_say(seq, n):
  for i in range(n):
    cur_seq = ''
    blocks = get_blocks(seq)
    for block in blocks:
      cur_seq += str(len(block)) + block[0]
    seq = cur_seq
  return seq

print('First part:', len(look_and_say(seq, 40)))
print('Second part:', len(look_and_say(seq, 50)))
