import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("안전영역.txt", "rt")


def DFS(px, py):
  ch[px][py] = 1
  for i in range(4):
    x = px + dx[i]
    y = py + dy[i]
    if 0 <= x < N and 0 <= y < N and arr[x][y] > idx and ch[x][y] == 0:
      DFS(x, y)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

minn = 214860000
maxx = 0

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
        DFS(i, j)

  res = max(cnt, res)

print(res)
