import sys

sys.stdin = open("이분검색.txt", "rt")

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

lp = 0
rp = N - 1
mid = (lp + rp) // 2

while arr[mid] != M:
  if arr[mid] > M:
    rp = mid - 1
  else:
    lp = mid + 1
  mid = (lp + rp) // 2
  if arr[mid] == M:
    break

print(mid + 1)
