import sys


def DFS(L, s):
  global res
  if L == M:
    sum = 0
    for j in range(len(house)):
      x1 = house[j][0]
      y1 = house[j][1]
      dis = 21470000
      for x in combi:
        x2 = pizza[x][0]
        y2 = pizza[x][1]
        dis = min(dis, abs(y2 - y1) + abs(x2 - x1))
      sum += dis
    if sum < res:
      res = sum
  else:
    for i in range(s, len(pizza)):
      combi[L] = i
      DFS(L + 1, i + 1)


sys.stdin = open("피자배달거리.txt", "rt")

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
house = []
pizza = []
combi = [0] * M  # 6C4
res = 21470000
for i in range(N):
  for j in range(N):
    if arr[i][j] == 1:
      house.append((i, j))
    elif arr[i][j] == 2:
      pizza.append((i, j))

DFS(0, 0)
print(res)
