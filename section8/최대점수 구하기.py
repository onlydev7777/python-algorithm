import sys

sys.stdin = open("최대점수 구하기.txt", "rt")

N, M = map(int, input().split())
dy = [0] * (M + 1)

for i in range(N):
  score, time = map(int, input().split())
  for j in range(M, time - 1, -1):
    temp = dy[j - time] + score
    dy[j] = max(dy[j], temp)

print(dy[M])
