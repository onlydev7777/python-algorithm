def solution(board):
  mine = []
  dx = [-1, -1, 0, 1, 1, 1, 0, -1]
  dy = [0, -1, -1, -1, 0, 1, 1, 1]
  n = len(board)
  for i in range(n):
    for j in range(len(board[i])):
      if board[i][j] == 1:
        mine.append((i, j))

  for x, y in mine:
    for i in range(8):
      xx = x + dx[i]
      yy = y + dy[i]
      if 0 <= xx < n and 0 <= yy < n:
        board[xx][yy] = 1
  cnt = 0

  for i in range(n):
    for j in range(len(board[i])):
      if board[i][j] == 0:
        cnt += 1

  return cnt


print(
    solution(
        [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0],
         [0, 0, 0, 0, 0]]))
