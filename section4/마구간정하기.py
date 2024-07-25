import sys

sys.stdin = open("마구간정하기.txt", "rt")

N, C = map(int, input().split())

lp = 214860000
rp = 0
arr = []

for _ in range(N):
  temp = int(input())
  if temp < lp:
    lp = temp
  if temp > rp:
    rp = temp
  arr.append(temp)

res = 0
arr.sort()

while lp <= rp:
  mid = (lp + rp) // 2
  cnt = 1
  idx = arr[0]
  for val in arr:
    if val - idx >= mid:
      idx = val
      cnt += 1
  if cnt < C:
    rp = mid - 1
  else:
    lp = mid + 1
    res = mid

print(res)
