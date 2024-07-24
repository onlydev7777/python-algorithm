import sys

sys.stdin = open("뮤직비디오.txt", "rt")

N, M = map(int, input().split())
arr = list(map(int, input().split()))

lt = 1
rt = sum(arr)
maxx = max(arr)
res = 0

while lt <= rt:
  mid = (lt + rt) // 2
  cnt = 1
  sec = 0
  for val in arr:
    if sec + val > mid:
      cnt += 1
      sec = val
    else:
      sec += val

  if mid >= maxx and cnt <= M:
    rt = mid - 1
    res = mid
  else:
    lt = mid + 1

print(res)
