import sys

sys.stdin = open("동전 바꿔주기.txt", "rt")


def DFS(L, summ):
  global cnt
  if summ > T:
    return
  elif L == K:
    if summ == T:
      cnt += 1
  else:
    for i in range(coinCnt[L] + 1):
      DFS(L + 1, summ + coin[L] * i)


T = int(input())
K = int(input())
coin = []
coinCnt = []
for _ in range(K):
  m, c = map(int, input().split())
  coin.append(m)
  coinCnt.append(c)

cnt = 0
DFS(0, 0)
print(cnt)
