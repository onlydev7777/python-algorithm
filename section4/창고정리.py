import sys

sys.stdin = open("창고정리.txt", "rt")

L = int(input())
arr = list(map(int, input().split()))
M = int(input())

maxx = max(arr)
minn = min(arr)

for _ in range(M):
  findMax = False
  findMin = False

  for i in range(L):
    if arr[i] > maxx:
      maxx = arr[i]
    if arr[i] < minn:
      minn = arr[i]

    if arr[i] == maxx and findMax == False:
      arr[i] -= 1
      maxx -= 1
      findMax = True
    elif arr[i] == minn and findMin == False:
      arr[i] += 1
      minn += 1
      findMin = True

res = max(arr) - min(arr)
print(res)

# 해싱으로 푸는 법

# cnt = [0] * 101
# maxH = float('-inf')
# minH = float('inf')
# for x in arr:
#   cnt[x] += 1
#   if x > maxH: maxH = x
#   if x < minH: minH = x
#
# for _ in range(M):
#   if cnt[maxH] == 1:
#     cnt[maxH] -= 1
#     maxH -= 1
#     cnt[maxH] += 1
#   else:
#     cnt[maxH] -= 1
#     cnt[maxH - 1] += 1
#
#   if cnt[minH] == 1:
#     cnt[minH] -= 1
#     minH += 1
#     cnt[minH] += 1
#   else:
#     cnt[minH] -= 1
#     cnt[minH + 1] += 1
#
# res = maxH - minH
# print(res)
