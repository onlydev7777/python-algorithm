import sys

sys.stdin = open("침몰하는타이타닉.txt", "rt")

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
print(arr)
lp = 0
rp = N - 1
cnt = 0

while lp <= rp:
  if arr[lp] + arr[rp] <= M:
    lp += 1
  rp -= 1
  cnt += 1

print(cnt)
