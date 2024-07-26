import sys

sys.stdin = open("역수열.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))
lst = [0] * N

for i in range(1, N + 1):
  val = arr[i - 1]
  cnt = -1
  for ii, vv in enumerate(lst):
    if vv == 0:
      cnt += 1
    if cnt == val:
      lst[ii] = i
      break;

for val in lst:
  print(val, end=' ')
