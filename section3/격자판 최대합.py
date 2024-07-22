import sys

sys.stdin = open("격자판 최대합.txt", "rt")

N = int(input())
arr = [[0] * N for _ in range(N)]

for i in range(N):
  arr[i] = list(map(int, input().split()))

sumArr = [0] * 4

for i in range(N):
  sum0 = 0
  sum1 = 0
  for j in range(N):
    sum0 += arr[i][j]  # 가로 합
    sum1 += arr[j][i]  # 세로 합

  if sum0 > sumArr[0]:
    sumArr[0] = sum0
  if sum1 > sumArr[1]:
    sumArr[1] = sum1

  sumArr[2] += arr[i][i]  # 대각선
  sumArr[3] += arr[i][N - i - 1]  # 반대편 대각선

maxSum = max(sumArr)

print(maxSum)
