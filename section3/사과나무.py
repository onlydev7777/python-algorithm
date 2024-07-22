import sys

sys.stdin = open("사과나무.txt", "rt")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
sum = 0
cen = N // 2
start = end = cen

for i in range(N):
  for j in range(start, end + 1):
    sum += arr[i][j]
  if i < cen:
    start -= 1
    end += 1
  else:
    start += 1
    end -= 1

print(sum)
