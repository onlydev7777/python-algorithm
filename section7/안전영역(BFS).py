import sys
from collections import deque

sys.stdin = open("안전영역.txt", "rt")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

minn = 214860000
maxx = 0
dq = deque()

for v in arr:
  rowMax = max(v)
  rowMin = min(v)
  if maxx < rowMax:
    maxx = rowMax
  if minn > rowMin:
    minn = rowMin

res = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for idx in range(minn, maxx + 1):
  cnt = 0
  ch = [[0] * N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      if arr[i][j] > idx and ch[i][j] == 0:
        cnt += 1
        dq.append((i, j))
        ch[i][j] = 1
        while dq:
          tmp = dq.popleft()
          for ii in range(4):
            x = tmp[0] + dx[ii]
            y = tmp[1] + dy[ii]
            if 0 <= x < N and 0 <= y < N and arr[x][y] > idx and ch[x][y] == 0:
              ch[x][y] = 1
              dq.append((x, y))

  res = max(res, cnt)

print(res)
