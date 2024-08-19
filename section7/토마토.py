import sys
from collections import deque

sys.stdin = open("토마토.txt", "rt")

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]

res = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dq = deque()
ch = [[0 for j in range(M)] for i in range(N)]
for i in range(N):
  for j in range(M):
    if arr[i][j] == 1 and ch[i][j] == 0:
      dq.append((i, j))

while dq:
  tmp = dq.popleft()
  for ii in range(4):
    x = tmp[0] + dx[ii]
    y = tmp[1] + dy[ii]
    if 0 <= x < N and 0 <= y < M and arr[x][y] == 0:
      arr[x][y] = 1
      ch[x][y] = ch[tmp[0]][tmp[1]] + 1
      dq.append((x, y))

for i in range(N):
  for j in range(M):
    if arr[i][j] == 0:
      print(-1)
      sys.exit(0)

    res = max(res, ch[i][j])

print(res)
