import sys

sys.stdin = open("동전교환.txt", "rt")


def DFS(L, sum):
  global minn
  if sum > M:
    return

  if minn < L:
    return

  if sum == M:
    if minn > L:
      minn = L
    return

  for v in arr:
    DFS(L + 1, sum + v)


N = int(input())
arr = list(map(int, input().split()))
M = int(input())
minn = 214860000
arr.sort(reverse=True)
DFS(0, 0)
print(minn)
