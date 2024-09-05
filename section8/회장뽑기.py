import sys

sys.stdin = open("회장뽑기.txt", "rt")

N = int(input())
dis = [[100] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
  dis[i][i] = 0

while True:
  s, e = map(int, input().split())
  if s == -1 and e == -1:
    break
  dis[s][e] = 1
  dis[e][s] = 1

for k in range(1, N + 1):
  for i in range(1, N + 1):
    for j in range(1, N + 1):
      dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

res = [0] * (N + 1)
score = 100
for i in range(1, N + 1):
  for j in range(1, N + 1):
    res[i] = max(res[i], dis[i][j])
  score = min(score, res[i])

lst = list()

for i in range(N + 1):
  if res[i] == score:
    lst.append(i)

print(score, len(lst))

for v in lst:
  print(v, end=' ')
