import sys

sys.stdin = open("부분집합구하기.txt", "rt")


def subset(v):
  if v == N + 1:
    for i in range(1, N + 1):
      if arr[i] == 1:
        print(i, end=' ')
    print()
    return
  arr[v] = 1
  subset(v + 1)
  arr[v] = 0
  subset(v + 1)


N = int(input())
arr = [0] * (N + 1)
subset(1)
