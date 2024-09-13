moves = open('1.txt').readline().strip().split(', ')

def first_part(moves):
    pos = [0, 0]
    cur_face = 0
    faces = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for move in moves:
        if move[0] == 'R':
            cur_face = (cur_face + 1) % 4
        else:
            cur_face = 3 if cur_face == 0 else cur_face - 1
        pos[0] += faces[cur_face][0] * int(move[1:])
        pos[1] += faces[cur_face][1] * int(move[1:])
    return abs(pos[0]) + abs(pos[1])

def second_part(moves):
    visited = {}
    pos = [0, 0]
    cur_face = 0
    faces = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for move in moves:
        if move[0] == 'R':
            cur_face = (cur_face + 1) % 4
        else:
            cur_face = 3 if cur_face == 0 else cur_face - 1
        prev_pos = pos[:]
        pos[0] += faces[cur_face][0] * int(move[1:])
        pos[1] += faces[cur_face][1] * int(move[1:])
        for i in range(1, int(move[1:]) + 1):
            cpos = (prev_pos[0] + faces[cur_face][0] * i, prev_pos[1] + faces[cur_face][1] * i)
            if cpos in visited:
                return abs(cpos[0]) + abs(cpos[1])
            visited[cpos] = 1

print('First part:', first_part(moves))
print('Second part:', second_part(moves))

