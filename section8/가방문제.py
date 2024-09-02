import sys

sys.stdin = open("가방문제.txt", "rt")

N, weight = map(int, input().split())
arr = [0] * N
dy = [0] * (weight + 1)
maxx = 0

for i in range(N):
  pWeight, pValue = map(int, input().split())
  for j in range(pWeight, weight + 1):
    temp = dy[j - pWeight] + pValue
    dy[j] = max(temp, dy[j])

print(dy[weight])
