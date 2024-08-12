import sys

sys.stdin = open("수들의 조합.txt")


def DFS(L, S):
  global cnt
  if L == K:
    if sum(res) % M == 0:
      # for v in res:
      #   print(v, end=' ')
      # print()
      cnt += 1
    return
  for i in range(S, N + 1):
    res[L] = arr[i - 1]
    DFS(L + 1, i + 1)


N, K = map(int, input().split())
arr = list(map(int, input().split()))
M = int(input())
cnt = 0
res = [0] * K

DFS(0, 1)
print(cnt)
