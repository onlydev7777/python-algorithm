import sys

sys.stdin = open("최대점수 구하기.txt", "rt")


def DFS(S, maxx, summ):
  global gmax
  if summ > M:
    return
  if gmax < maxx:
    gmax = maxx
  for i in range(S, N):
    DFS(i + 1, arr[i][0] + maxx, arr[i][1] + summ)


def DFS2(L, maxx, summ):
  global gmax
  if summ > M:
    return
  if L == N:
    if gmax < maxx:
      gmax = maxx
  else:
    DFS2(L + 1, arr[L][0] + maxx, arr[L][1] + summ)
    DFS2(L + 1, maxx, summ)


N, M = map(int, input().split())
arr = []

for _ in range(N):
  arr.append(tuple(map(int, input().split())))

gmax = 0
DFS(0, 0, 0)
print(gmax)
gmax = 0
DFS2(0, 0, 0)
print(gmax)
