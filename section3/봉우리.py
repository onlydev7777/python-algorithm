import sys

sys.stdin = open("봉우리.txt", "rt")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

for i in range(N):
  for j in range(N):
    me = arr[i][j]
    left = 0 if i - 1 < 0 else arr[i - 1][j]
    right = 0 if i + 1 == N else arr[i + 1][j]
    up = 0 if j - 1 < 0 else arr[i][j - 1]
    down = 0 if j + 1 == N else arr[i][j + 1]
    if me > left and me > right and me > up and me > down:
      cnt += 1

print(cnt)
