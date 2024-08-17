import sys
from collections import deque

sys.stdin = open("단지 번호 붙이기.txt", "rt")

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = []
dq = deque()

for i in range(N):
  for j in range(N):
    if arr[i][j] == 1:
      cnt = 1
      arr[i][j] = 0
      dq.append((i, j))
      while dq:
        tmp = dq.popleft()
        for ii in range(4):
          x = tmp[0] + dx[ii]
          y = tmp[1] + dy[ii]
          if 0 <= x < N and 0 <= y < N and arr[x][y] == 1:
            arr[x][y] = 0
            cnt += 1
            dq.append((x, y))
      else:
        res.append(cnt)
        
print(len(res))
res.sort()
for v in res:
  print(v)
