import sys

sys.stdin = open("양팔저울.txt", "rt")


def DFS(L, l, r):
  if L == K:
    ch[abs(r - l)] = 1
  else:
    DFS(L + 1, l + arr[L], r)
    DFS(L + 1, l, r)
    DFS(L + 1, l, r + arr[L])


def DFS2(L, paramSumm):
  if L == K:
    if 0 < paramSumm < summ:
      ch[paramSumm] = 1
  else:
    DFS2(L + 1, paramSumm + arr[L])
    DFS2(L + 1, paramSumm - arr[L])
    DFS2(L + 1, paramSumm)


K = int(input())
arr = list(map(int, input().split()))
summ = sum(arr)
ch = [0] * (summ + 1)
cnt = 0

DFS(0, 0, 0)

for i in range(1, summ):
  if ch[i] == 0:
    cnt += 1
print(cnt)

ch = [0] * (summ + 1)
cnt = 0
DFS2(0, 0)
for i in range(1, summ):
  if ch[i] == 0:
    cnt += 1
print(cnt)
