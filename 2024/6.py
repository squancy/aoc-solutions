from collections import defaultdict

blocks = []
size = None
pos = None

with open("6.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    size = (len(lines), len(lines[0]))
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '^':
                pos = (i, j)
            elif lines[i][j] == '#':
                blocks.append((i, j))

def first_part(blocks, pblock = []):
    ps = set((pos,))
    cur_pos = (pos[0], pos[1])
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    cur_dir_ind = 0
    track = defaultdict(list)
    while True:
        if not (0 <= cur_pos[0] < size[0]) or not (0 <= cur_pos[1] < size[1]):
            if not pblock:
                return len(ps) - 1, ps
            else:
                return 0
        new_pos = (cur_pos[0] + dirs[cur_dir_ind][0], cur_pos[1] + dirs[cur_dir_ind][1])
        if new_pos in blocks:
            cur_dir_ind = (cur_dir_ind + 1) % 4
            if cur_pos in track and cur_dir_ind in track[cur_pos] and pblock:
                return 1
        else:
            cur_pos = new_pos
            ps |= set((new_pos,))
        track[cur_pos].append(cur_dir_ind)

def second_part(possible_blocks):
    res = 0
    i = 1
    for pb in possible_blocks:
        res += first_part(blocks + [pb], pb) 
        i += 1
    return res

fpres, possible_blocks = first_part(blocks)

print("First part:", fpres)
# this naive approach takes a min or two to run
print("Second part:", second_part(possible_blocks))

