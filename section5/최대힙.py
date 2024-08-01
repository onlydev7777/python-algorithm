import heapq
import sys

sys.stdin = open("최대힙.txt", "rt")
arr = []

while True:
  data = int(input())
  if data == -1:
    break
  if data == 0:
    if len(arr) == 0:
      print(-1)
      break
    max = heapq.heappop(arr) * -1
    print(max)
  else:
    heapq.heappush(arr, data * -1)
