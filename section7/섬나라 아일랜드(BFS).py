import sys
from collections import deque

sys.stdin = open("섬나라 아일랜드.txt", "rt")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dq = deque()

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
cnt = 0
for i in range(N):
  for j in range(N):
    if arr[i][j] == 1:
      cnt += 1
      dq.append((i, j))
      while dq:
        tmp = dq.popleft()
        for ii in range(8):
          x = tmp[0] + dx[ii]
          y = tmp[1] + dy[ii]
          if 0 <= x < N and 0 <= y < N and arr[x][y] == 1:
            arr[x][y] = 0
            dq.append((x, y))

print(cnt)
