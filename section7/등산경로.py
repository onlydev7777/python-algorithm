import sys

sys.stdin = open("등산경로.txt", "rt")


def DFS(prev, px, py):
  global cnt
  if prev == maxx:
    cnt += 1
    return
  for i in range(4):
    x = px + dx[i]
    y = py + dy[i]
    if 0 <= x < N and 0 <= y < N and ch[x][y] == 0 and arr[x][y] > prev:
      ch[x][y] = 1
      DFS(arr[x][y], x, y)
      ch[x][y] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ch = [[0] * N for _ in range(N)]

maxx = 0
minn = 214860000
sx = 0
sy = 0
for i in range(N):
  for j in range(N):
    if maxx < arr[i][j]:
      maxx = arr[i][j]
    if minn > arr[i][j]:
      minn = arr[i][j]
      sx = i
      sy = j

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
ch[sx][sy] = 1
DFS(minn, sx, sy)
print(cnt)
