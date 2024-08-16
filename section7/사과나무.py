import sys
from collections import deque

sys.stdin = open("사과나무.txt", "rt")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
s = N // 2
ch = [[0] * N for _ in range(N)]
ch[s][s] = 1
sum = arr[s][s]
dq = deque()
dq.append((s, s))
loop = 0

while loop < s:
  size = len(dq)
  for i in range(size):
    tmp = dq.popleft()
    for j in range(4):
      x = tmp[0] + dx[j]
      y = tmp[1] + dy[j]
      if ch[x][y] == 0:
        sum += arr[x][y]
        ch[x][y] = 1
        dq.append((x, y))
  loop += 1

print(sum)
