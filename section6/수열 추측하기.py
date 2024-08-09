import sys

sys.stdin = open("수열 추측하기.txt", "rt")


def DFS(L):
  if L == N:
    sum = 0
    for i in range(N):
      sum = sum + (b[i] * arr[i])
    if sum == F:
      for i in arr:
        print(i, end=' ')
      sys.exit(0)
  for i in range(1, N + 1):
    if ch[i] == 0:
      ch[i] = 1
      arr[L] = i
      DFS(L + 1)
      ch[i] = 0


N, F = map(int, input().split())
arr = [0] * N
b = [1] * N
ch = [0] * (N + 1)
for i in range(1, N):
  b[i] = b[i - 1] * (N - i) // i

DFS(0)
