def first_part():
    ranges, ids = ranges_and_ids()
    res = 0
    for ID in ids:
        for r in ranges:
            if r[0] <= ID <= r[1]:
                res += 1
                break
    return res

def second_part():
    ranges, _ = ranges_and_ids()
    start_pos = sorted(set([x[0] for x in ranges]))
    end_pos = sorted(set([x[1] for x in ranges]))
    intervals = []
    cur_pos = start_pos[0]
    start_ind = 0
    end_ind = 0
    prev_step = "start"
    while start_ind < len(start_pos):
        cur_pos_save = cur_pos
        if end_pos[end_ind] < start_pos[start_ind]:
            cur_pos = end_pos[end_ind] 
            end_ind += 1
            intervals.append([cur_pos_save, cur_pos])
            prev_step = "end"
        else:
            cur_pos = start_pos[start_ind]
            start_ind += 1
            if prev_step == "start" or (prev_step == "end" and find_int(cur_pos_save, cur_pos, ranges)): intervals.append([cur_pos_save, cur_pos])
            prev_step = "start" 
    intervals.append([cur_pos, end_pos[-1]])
    s = intervals[0][0]
    ints = []
    for i in range(len(intervals)):
        if i == len(intervals) - 1:
            ints.append([s, intervals[-1][1]])
            break
        if intervals[i][1] != intervals[i + 1][0]:
            ints.append([s, intervals[i][1]])
            s = intervals[i + 1][0]
    return sum(x[1] - x[0] + 1 for x in ints)

def find_int(s, e, ranges):
    for r in ranges:
        if r[0] <= s and r[1] >= e: return True
    return False

def ranges_and_ids():
    ranges, ids = [], []
    flag = True
    for line in open("5.txt").readlines():
        line = line.strip()
        if not line:
            flag = False
            continue
        if flag:
            ranges.append([int(x) for x in line.split("-")])
        else:
            ids.append(int(line))
    return ranges, ids    
    
print("First part:", first_part())
print("Second part:", second_part())
