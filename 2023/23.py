lines = [x.strip() for x in open('23.txt').readlines()] 

def run(cl, a, b):
    while True:
        if cl < 0 or cl >= len(lines):
            break
        cmd = lines[cl]
        r = cmd.split(' ')[1].replace(',', ' ').strip()
        jumped = False
        if cmd.startswith('hlf'):
            if r == 'a':
                a /= 2
            else:
                b /= 2
        elif cmd.startswith('tpl'):
            if r == 'a':
                a *= 3
            else:
                b *= 3
        elif cmd.startswith('inc'):
            if r == 'a':
                a += 1
            else:
                b += 1
        elif cmd.startswith('jmp'):
            cl += int(r)
            jumped = True
        elif cmd.startswith('jie'):
            if (r == 'a' and a % 2 == 0) or (r == 'b' and b % 2 == 0):
                cl += int(cmd.split(', ')[1])
                jumped = True
        elif cmd.startswith('jio'):
            if (r == 'a' and a == 1) or (r == 'b' and b == 1):
                cl += int(cmd.split(', ')[1])
                jumped = True
        if not jumped:
            cl += 1
    return int(b)

def first_part(lines):
    cl, a, b = 0, 0, 0
    return run(cl, a, b)

def second_part(lines):
    cl, a, b = 0, 1, 0
    return run(cl, a, b)

print('First part:', first_part(lines))
print('Second part:', second_part(lines))
