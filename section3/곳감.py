import sys

sys.stdin = open("곳감.txt", "rt")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
M = int(input())

for _ in range(M):
  row, dir, cnt = map(int, input().split())

  if dir == 0:  # left
    for _ in range(cnt):
      arr[row - 1].append(arr[row - 1].pop(0))
  else:  # right
    for _ in range(cnt):
      arr[row - 1].insert(0, arr[row - 1].pop())

sum = 0
start = 0
end = N - 1
cen = N // 2

for i in range(N):
  for j in range(start, end + 1):
    sum += arr[i][j]
  if i < cen:
    start += 1
    end -= 1
  else:
    start -= 1
    end += 1

print(sum)
