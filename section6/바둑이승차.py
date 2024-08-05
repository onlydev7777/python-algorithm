import sys

sys.stdin = open("바둑이승차.txt", "rt")


def DFS(level, sum, tsum):
  global max
  if sum > C:
    return
  if sum + (total - tsum) < max:
    return
  if level == N:
    if max < sum:
      max = sum
  else:
    DFS(level + 1, sum + arr[level], tsum + arr[level])
    DFS(level + 1, sum, tsum + arr[level])


C, N = map(int, input().split())
arr = []
max = 0

for _ in range(N):
  arr.append(int(input()))

total = sum(arr)
DFS(0, 0, 0)
print(max)
