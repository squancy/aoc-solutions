f = open('inp4.txt')
nums = [int(x) for x in f.readline().split(',')]
boards = []
board = []
for line in f.readlines():
  line = line.lstrip().rstrip()
  if len(line) == 0:
    boards.append(board)
    board = []
  else:
    board.append([int(x.lstrip().rstrip()) for x in line.split(' ') if x])

def check_rows(boards):
  brds = []
  for i in range(len(boards)):
    board = boards[i]
    for row in board:
      flag = False
      for el in row:
        if el != None:
          flag = True
          break
      if not flag:
        brds.append(i)
        break
  return brds

def check_columns(boards):
  brds = []
  for i in range(len(boards)):
    board = boards[i]
    for col_num in range(len(board[0])):
      flag = False
      for k in range(len(board)):
        if board[k][col_num] != None:
          flag = True 
          break
      if not flag:
        brds.append(i)
        break
  return brds

def get_score(board, n):
  summa = 0
  for row in board:
    for el in row:
      if el != None:
        summa += el
  return summa * n

first_part = True
for n in nums:
  for i in range(len(boards)):
    for j in range(len(boards[i])):
      for k in range(len(boards[i][j])):
        if boards[i][j][k] == n:
          boards[i][j][k] = None

  b1 = check_rows(boards)
  b2 = check_columns(boards)
  b1.extend(b2)
  last_board = boards[0]
  for i in range(len(boards)):
    if i in b1:
      if first_part:
        first_part = False
        print('First part:', get_score(boards[i], n))
      boards[i] = None

  l = 0
  while l < len(boards):
    if boards[l] == None:
      del boards[l]
      l -= 1
    l += 1

  if len(boards) == 0:
    print('Second part:', get_score(last_board, n))
    break
