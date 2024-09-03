import sys

sys.stdin = open("동전교환.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))
won = int(input())

dy = [1000] * (won + 1)
dy[0] = 0

for i in range(N):
  coin = arr[i]
  for j in range(coin, won + 1):
    temp = dy[j - coin] + 1
    dy[j] = min(dy[j], temp)

print(dy[won])
