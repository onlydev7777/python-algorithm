import sys
from collections import deque

sys.stdin = open("응급실.txt", "rt")

N, M = map(int, input().split())
arr = list(map(int, input().split()))

deq = deque()
for i, v in enumerate(arr):
  deq.append((v, i))

cnt = 0
while True:
  data = deq.popleft()
  if data[0] < max(deq)[0]:
    deq.append(data)
  else:
    cnt += 1
    if data[1] == M:
      print(cnt)
      break
