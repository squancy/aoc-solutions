lines = [line.strip() for line in open('11.txt').readlines()]

def inc_first_coord(k, coord_to_inc, galaxies, C):
    for i in range(len(galaxies)):
        if galaxies[i][0] > k:
            if galaxies[i] in coord_to_inc:
                coord_to_inc[galaxies[i]][0] += C
            else:
                coord_to_inc[galaxies[i]] = [C, 0]
            
def inc_second_coord(k, coord_to_inc, galaxies, C):
    for i in range(len(galaxies)):
        if galaxies[i][1] > k:
            if galaxies[i] in coord_to_inc:
                coord_to_inc[galaxies[i]][1] += C
            else:
                coord_to_inc[galaxies[i]] = [0, C]

def sum_dist(galaxies):
    sum = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            sum += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
    return sum

def solve(lines, C):
    galaxies = []
    coord_to_inc = {}
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                galaxies.append((i, j))

    for i in range(len(lines)):
        if lines[i].count('.') == len(lines[i]):
            inc_first_coord(i, coord_to_inc, galaxies, C)

    for i in range(len(lines[0])):
        flag = True
        for j in range(len(lines)):
            if lines[j][i] == '#':
                flag = False
                break
        if flag:
            inc_second_coord(i, coord_to_inc, galaxies, C)
    
    for k, v in coord_to_inc.items():
        ind = galaxies.index(k)
        galaxies[ind] = (galaxies[ind][0] + v[0], galaxies[ind][1] + v[1])
    return sum_dist(galaxies)

def first_part(lines):
    return solve(lines, 1)

def second_part(lines):
    return solve(lines, 10 ** 6 - 1)

print('First part:', first_part(lines))
print('Second part:', second_part(lines))

