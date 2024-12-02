lines = [[int(x) for x in line.split(' ')] for line in open("2.txt").readlines()]

def diff(arr):
    for i in range(1, len(arr)):
        if not (1 <= abs(arr[i - 1] - arr[i]) <= 3):
            return False
    return True

def first_part():
    cnt = 0
    for line in lines:
        if (sorted(line) == line or sorted(line, reverse=True) == line) and diff(line):
            cnt += 1
    return cnt

def second_part():
    cnt = 0
    for line in lines:
        if (sorted(line) == line or sorted(line, reverse=True) == line) and diff(line):
            cnt += 1
            continue
        for i in range(len(line)):
            mline = line[:i] + line[i + 1:]
            if (sorted(mline) == mline or sorted(mline, reverse=True) == mline) and diff(mline):
                cnt += 1
                break
    return cnt

print("First part:", first_part())
print("Second part:", second_part())
            
