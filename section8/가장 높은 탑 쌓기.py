import sys

sys.stdin = open("가장 높은 탑 쌓기.txt", "rt")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dy = [0] * N
dy[0] = arr[0][1]
res = arr[0][1]

arr.sort(key=lambda x: x[0], reverse=True)
for v in arr:
  print(v)
  
for i in range(1, N):
  maxx = 0
  for j in range(i - 1, -1, -1):
    if arr[i][2] < arr[j][2]:
      if maxx < dy[j]:
        maxx = dy[j]
  dy[i] = maxx + arr[i][1]
  if res < dy[i]:
    res = dy[i]

print(res)
print(dy)
