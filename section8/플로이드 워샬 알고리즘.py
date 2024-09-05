import sys

sys.stdin = open("플로이드 워샬 알고리즘.txt", "rt")

N, M = map(int, input().split())
dis = [[5000] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
  dis[i][i] = 0

for i in range(M):
  s, e, l = map(int, input().split())
  dis[s][e] = l

for k in range(1, N + 1):
  for i in range(1, N + 1):
    for j in range(1, N + 1):
      dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

for i in range(1, N + 1):
  for j in range(1, N + 1):
    if dis[i][j] == 5000:
      print('M', end=' ')
    else:
      print(dis[i][j], end=' ')
  print()
  