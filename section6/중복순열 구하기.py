import sys

sys.stdin = open("중복순열 구하기.txt", "rt")


def DFS(L):
  global cnt
  if L == M:
    for j in arr:
      print(j, end=' ')
    cnt = cnt + 1
    print()
    return
  for i in range(1, N + 1):
    arr[L] = i
    DFS(L + 1)


N, M = map(int, input().split())
arr = [0] * M
cnt = 0
DFS(0)
print(cnt)
