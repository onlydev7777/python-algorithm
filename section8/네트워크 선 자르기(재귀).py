import sys


def DFS(L):
  if dy[L] > 0:
    return dy[L]
  if L < 3:
    return L

  dy[L] = DFS(L - 1) + DFS(L - 2)
  return dy[L]


sys.stdin = open("네트워크 선 자르기.txt", "rt")

N = int(input())
dy = [0] * (N + 1)
dy[1] = 1
dy[2] = 2

DFS(N)

print(dy[N])
