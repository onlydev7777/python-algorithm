import copy
import sys
from collections import deque

sys.stdin = open("미로의 최단경로.txt", "rt")

arr = [list(map(int, input().split())) for _ in range(7)]
arr2 = copy.deepcopy(arr)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
dq = deque()
dq.append((0, 0))

# 2차원 거리 배열 방식
while dq:
  tmp = dq.popleft()
  for i in range(4):
    x = tmp[0] + dx[i]
    y = tmp[1] + dy[i]
    if 0 <= x <= 6 and 0 <= y <= 6 and arr[x][y] == 0:
      arr[x][y] = arr[tmp[0]][tmp[1]] + 1
      dq.append((x, y))

if arr[6][6] == 0:
  print(-1)
else:
  print(arr[6][6])

# size 방식
L = 0
dq = deque()
dq.append((0, 0))
while True:
  size = len(dq)
  if size == 0:
    print(-1)
    break
  for i in range(size):
    tmp = dq.popleft()
    if tmp[0] == 6 and tmp[1] == 6:
      print(L)
      sys.exit(0)
    for j in range(4):
      x = tmp[0] + dx[j]
      y = tmp[1] + dy[j]
      if 0 <= x <= 6 and 0 <= y <= 6 and arr2[x][y] == 0:
        arr2[x][y] = arr2[tmp[0]][tmp[1]] + 1
        dq.append((x, y))
  L += 1
