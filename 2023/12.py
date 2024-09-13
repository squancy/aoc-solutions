lines = [[x.strip().split(' ')[0], [int(y) for y in x.strip().split(' ')[1].split(',')]] for x in open('12.txt').readlines()]

def valid(line, actual_blocks):
    sp = line.split('.')
    blocks = []
    for p in sp:
        if not p: continue
        blocks.append(len(p))
    return blocks == actual_blocks

def count_arrangements(line_pair):
    current_line = line_pair[0]
    blocks = line_pair[1]
    if current_line.count('?') == 0 and valid(current_line, blocks):
        return 1
    elif current_line.count('?') == 0:
        return 0
    return count_arrangements([current_line.replace('?', '#', 1), blocks]) + count_arrangements([current_line.replace('?', '.', 1), blocks])

def first_part(lines):
    s = 0
    for line in lines:
        print(line, count_arrangements(line))
        s += count_arrangements(line)
    return s

print('First part:', first_part(lines))
