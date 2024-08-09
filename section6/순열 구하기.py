import sys

sys.stdin = open("순열 구하기.txt", "rt")


def DFS(L):
  global cnt
  if L == M:
    for i in range(M):
      print(arr[i], end=' ')
    cnt += 1
    print()
    return
  for i in range(1, N + 1):
    if ch[i] == 0:
      ch[i] = 1
      arr[L] = i
      DFS(L + 1)
      ch[i] = 0


N, M = map(int, input().split())
arr = [0] * M
ch = [0] * (N + 1)
cnt = 0
DFS(0)
print(cnt)
