import sys

sys.stdin = open("수들의 합.txt", "rt")

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 내가 짠 방식... 성능 좋지 못함... O(N^2)
# cnt = 0
# for i in range(n):
#   if arr[i] == m:
#     cnt += 1
#   elif arr[i] < m:
#     res = arr[i]
#     for j in range(i + 1, n):
#       res += arr[j]
#       if res == m:
#         cnt += 1
#         break
#       elif res > m:
#         break

# 강의 방식... 성능 좋음... O(N)
cnt = 0
tot = arr[0]
lp = 0
rp = 1

while True:
  if tot == m:
    cnt += 1
    tot -= arr[lp]
    lp += 1
  elif tot < m:
    if rp == n:
      break
    tot += arr[rp]
    rp += 1
  else:
    tot -= arr[lp]
    lp += 1

print(cnt)
