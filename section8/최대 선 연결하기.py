import sys

sys.stdin = open("최대 선 연결하기.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))
dy = [0] * N
dy[0] = 1
res = 0

for i in range(1, N):
  maxx = 0
  for j in range(0, i):
    if arr[i] > arr[j]:
      if maxx < dy[j]:
        maxx = dy[j]

  dy[i] = maxx + 1
  if res < dy[i]:
    res = dy[i]

print(res)
