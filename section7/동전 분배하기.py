import sys

sys.stdin = open("동전 분배하기.txt", "rt")


def DFS(L):
  global res
  if L == N:
    diff = max(money) - min(money)
    if res > diff:
      tmp = set()
      for i in range(3):
        tmp.add(money[i])
      if len(tmp) == 3:
        res = diff
    return
  for i in range(3):
    money[i] += arr[L]
    DFS(L + 1)
    money[i] -= arr[L]


N = int(input())
arr = []
for _ in range(N):
  arr.append(int(input()))

res = max(arr)
money = [0] * 3
DFS(0)
print(res)
