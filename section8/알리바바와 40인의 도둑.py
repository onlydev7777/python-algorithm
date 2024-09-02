import sys

sys.stdin = open("알리바바와 40인의 도둑.txt", "rt")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [0, -1]
dy = [-1, 0]

dyArr = [[0] * N for _ in range(N)]

dyArr[0][0] = arr[0][0]

for x in range(N):
  for y in range(N):
    minn = 214860000
    for k in range(2):
      xx = x + dx[k]
      yy = y + dy[k]
      if 0 <= xx < N and 0 <= yy < N:
        prevData = dyArr[xx][yy]
        minn = min(minn, prevData)

    if dyArr[x][y] == 0:
      dyArr[x][y] = minn + arr[x][y]

print(dyArr[N - 1][N - 1])
