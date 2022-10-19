hex_packet = open('inp16.txt').readline().lstrip().rstrip()
assoc = {
  '0': '0000',
  '1': '0001',
  '2': '0010',
  '3': '0011',
  '4': '0100',
  '5': '0101',
  '6': '0110',
  '7': '0111',
  '8': '1000',
  '9': '1001',
  'A': '1010',
  'B': '1011',
  'C': '1100',
  'D': '1101',
  'E': '1110',
  'F': '1111'
}

def perform_op(type_id, vals):
  if type_id == 0:
    return sum(vals)
  elif type_id == 1:
    prod = 1
    for v in vals:
      prod *= v
    return prod
  elif type_id == 2:
    return min(vals)
  elif type_id == 3:
    return max(vals)
  elif type_id == 5:
    return vals[0] > vals[1]
  elif type_id == 6:
    return vals[0] < vals[1] 
  elif type_id == 7:
    return vals[0] == vals[1]

packet = ''.join([assoc[d] for d in hex_packet])

def extract_packet(packet, acc, start, end):
  cur_packet = packet[start:end]
  if cur_packet.count('0') == len(cur_packet):
    return
  version = int('0b' + cur_packet[:3], base=2)
  type_id = int('0b' + cur_packet[3:6], base=2)
  acc[0] += version

  # literal
  if type_id == 4:
    enc_n = ''
    groups = []
    last_index = None
    for i in range(6, len(cur_packet)):
      if (i - 5) % 5 == 0:
        groups.append(cur_packet[i - 4:i + 1])
        if cur_packet[i - 4:i + 1][0] == '0':
          last_index = start + i + 1
          break
    for group in groups:
      enc_n += group[1:] 
      if group[0] == '0':
        break
    return last_index, int('0b' + enc_n, base=2)
  # operator
  else:
    len_type_id = cur_packet[6]
    vals = []
    if int(len_type_id) == 0:
      tot_len = int('0b' + cur_packet[7:22], base=2)

      # parse current package
      packet_start = start + 22
      packet_end = start + 22 + tot_len
      while packet_start != packet_end:
        packet_start, v = extract_packet(packet, acc, packet_start, packet_end)
        vals.append(v)
    else:
      num_of_packets = int('0b' + cur_packet[7:18], base=2)

      # parse current package
      packet_start = start + 18
      for i in range(num_of_packets):
        packet_start, v = extract_packet(packet, acc, packet_start, len(packet))
        vals.append(v)

    res = perform_op(type_id, vals)
    return packet_start, res

a = [0]
res = extract_packet(packet, a, 0, len(packet))[1]
print('First part:', a[0])
print('Second part:', res)
