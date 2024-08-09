import sys

sys.stdin = open("조합 구하기.txt", "rt")


def DFS(L, S):
  global cnt
  if L == M:
    for i in arr:
      print(i, end=' ')
    print()
    cnt += 1
    return
  for i in range(S, N + 1):
    arr[L] = i
    DFS(L + 1, i + 1)


N, M = map(int, input().split())

arr = [0] * M
cnt = 0
DFS(0, 1)
print(cnt)
