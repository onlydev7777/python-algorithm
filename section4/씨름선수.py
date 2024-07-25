import sys

sys.stdin = open("씨름선수.txt", "rt")

N = int(input())
arr = []
for _ in range(N):
  height, weight = map(int, input().split())
  arr.append((height, weight))

arr.sort(reverse=True)

weightMax = 0
cnt = 0
for height, weight in arr:
  if weight > weightMax:
    weightMax = weight
    cnt += 1

print(cnt)
