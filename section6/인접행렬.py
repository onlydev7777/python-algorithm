import sys

sys.stdin = open("인접행렬.txt", "rt")

N, M = map(int, input().split())
arr = [[0] * N for _ in range(N)]

for _ in range(M):
  row, col, data = map(int, input().split())
  arr[row - 1][col - 1] = data

for i in range(N):
  for j in range(N):
    print(arr[i][j], end=' ')
  print()
