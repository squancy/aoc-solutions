lines = [x.strip() for x in open('2.txt').readlines()]

def first_part(lines):
    code = ''
    moves = {
        1: {'L': 1, 'U': 1, 'R': 2, 'D': 4},
        2: {'L': 1, 'U': 2, 'R': 3, 'D': 5},
        3: {'L': 2, 'U': 3, 'R': 3, 'D': 6},
        4: {'L': 4, 'U': 1, 'R': 5, 'D': 7},
        5: {'L': 4, 'U': 2, 'R': 6, 'D': 8},
        6: {'L': 5, 'U': 3, 'R': 6, 'D': 9},
        7: {'L': 7, 'U': 4, 'R': 8, 'D': 7},
        8: {'L': 7, 'U': 5, 'R': 9, 'D': 8},
        9: {'L': 8, 'U': 6, 'R': 9, 'D': 9}
    }
    cur_pos = 5
    for line in lines:
        print(cur_pos)
        for c in line:
            cur_pos = moves[cur_pos][c]
        code += str(cur_pos)
    return code

print('First part:', first_part(lines))
