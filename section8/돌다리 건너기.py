import sys

sys.stdin = open("돌다리 건너기.txt", "rt")

N = int(input())
dy = [0] * (N + 2)
dy[1] = 1
dy[2] = 2

for i in range(3, N + 2):
  dy[i] = dy[i - 1] + dy[i - 2]

print(dy[N + 1])
