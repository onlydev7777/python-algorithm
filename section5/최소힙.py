import heapq
import sys

sys.stdin = open("최소힙.txt", "rt")
arr = list()

while True:
  data = int(input())
  if data == -1:
    break
  elif data == 0:
    if len(arr) == 0:
      print(-1)
    else:
      min = heapq.heappop(arr)
      print(min)
  else:
    heapq.heappush(arr, data)
