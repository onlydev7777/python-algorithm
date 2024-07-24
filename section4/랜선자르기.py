import sys

sys.stdin = open("랜선자르기.txt", "rt")

K, N = map(int, input().split())
arr = []
largest = 0
for _ in range(K):
  temp = int(input())
  arr.append(temp)
  largest = max(largest, temp)

lp = 1
rp = largest
res = 0
while lp <= rp:
  mid = (lp + rp) // 2
  cnt = 0
  for val in arr:
    cnt += val // mid
  if cnt < N:
    rp = mid - 1
  else:
    res = mid
    lp = mid + 1

print(res)
