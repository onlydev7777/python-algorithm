import sys

sys.stdin = open("단지 번호 붙이기.txt", "rt")


def DFS(px, py):
  global cnt
  for i in range(4):
    x = px + dx[i]
    y = py + dy[i]
    if 0 <= x < N and 0 <= y < N and arr[x][y] == 1:
      cnt += 1
      arr[x][y] = 0
      DFS(x, y)


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = []

for i in range(N):
  for j in range(N):
    if arr[i][j] == 1:
      arr[i][j] = 0
      cnt = 1
      DFS(i, j)
      res.append(cnt)

print(len(res))
res.sort()
for v in res:
  print(v)
