def parse_input():
    weapons, armor, rings = [], [], []
    lines = [line.strip() for line in open('gear_stats.txt').readlines()]
    switch = None
    for line in lines:
        if not line:
            continue

        if line.startswith("Weapons"):
            switch = 1
            continue
        elif line.startswith("Armor"):
            switch = 2
            continue
        elif line.startswith("Rings"):
            switch = 3
            continue
        
        parts = ' '.join(line.split()).split()
        t, c, d, a = parts[0], int(parts[1]), int(parts[2]), int(parts[3])
        if switch == 1:
            weapons.append({'t': t, 'c': c, 'd': d, 'a': a})
        elif switch == 2:
            armor.append({'t': t, 'c': c, 'd': d, 'a': a})
        else:
            rings.append({'t': t + str(c), 'c': d, 'd': a, 'a': int(parts[4])})

    armor.append({'t': 'no armor', 'c': 0, 'd': 0, 'a': 0})
    return weapons, armor, rings 

def ring_pairs(rings):
    pairs = [{'t': 'no ring', 'c': 0, 'd': 0, 'a': 0}]
    for r in rings:
        pairs.append({'t': r['t'], 'c': r['c'], 'a': r['a'], 'd': r['d']})
    for i in range(len(rings)):
        for j in range(len(rings)):
            if i == j: continue
            pairs.append({'t': rings[i]['t'] + rings[j]['t'], 'c': rings[i]['c'] + rings[j]['c'], 'd': rings[i]['d'] + rings[j]['d'], 'a': rings[i]['a'] + rings[j]['a']})
    return pairs

def get_enemy_stats():
    lines = open('21.txt').readlines()
    x = [int(x.split(':')[1].strip()) for x in lines]
    return {'life': x[0], 'd': x[1], 'a': x[2]}

def simulate_fight(player, enemy):
    turn = 1
    while True:
        if enemy['life'] <= 0:
            return True
        elif player['life'] <= 0:
            return False
        if turn:
            enemy['life'] -= max(1, player['d'] - enemy['a'])
        else:
            player['life'] -= max(1, enemy['d'] - player['a'])
        turn = not turn
        
def first_part():
    weapons, armor, rings = parse_input()
    min_gold = float('inf')
    for w in weapons:
        for a in armor:
            for r in ring_pairs(rings):
                d_score, a_score = w['d'] + a['d'] + r['d'], w['a'] + a['a'] + r['a']
                gold = w['c'] + a['c'] + r['c']
                player = {'d': d_score, 'a': a_score, 'life': 100}
                enemy = get_enemy_stats()
                if simulate_fight(player, enemy) and gold < min_gold:
                    min_gold = gold
    return min_gold

def second_part():
    weapons, armor, rings = parse_input()
    min_gold = float('inf')
    for w in weapons:
        for a in armor:
            for r in ring_pairs(rings):
                d_score, a_score = w['d'] + a['d'] + r['d'], w['a'] + a['a'] + r['a']
                gold = w['c'] + a['c'] + r['c']
                player = {'d': d_score, 'a': a_score, 'life': 100}
                enemy = get_enemy_stats()
                if simulate_fight(player, enemy) and gold < min_gold:
                    min_gold = gold
    return min_gold

def second_part():
    weapons, armor, rings = parse_input()
    max_gold = 0
    for w in weapons:
        for a in armor:
            for r in ring_pairs(rings):
                d_score, a_score = w['d'] + a['d'] + r['d'], w['a'] + a['a'] + r['a']
                gold = w['c'] + a['c'] + r['c']
                player = {'d': d_score, 'a': a_score, 'life': 100}
                enemy = get_enemy_stats()
                if not simulate_fight(player, enemy) and gold > max_gold:
                    max_gold = gold
    return max_gold

print('First part:', first_part())
print('Second part:', second_part())
