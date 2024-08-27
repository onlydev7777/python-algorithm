import sys

sys.stdin = open("계단오르기.txt", "rt")


def DFS(L):
  if L < 3:
    return L
  if dy[L] > 0:
    return dy[L]
  dy[L] = DFS(L - 1) + DFS(L - 2)
  return dy[L]


N = int(input())
dy = [0] * (N + 1)

DFS(N)
print(dy[N])
