import sys
from collections import deque

sys.stdin = open("공주구하기.txt", "rt")

N, K = map(int, input().split())

deq = deque(list(range(1, N + 1)))

idx = 1
data = 0
while deq:
  data = deq.popleft()
  if idx < K:
    deq.append(data)
    idx += 1
  else:
    idx = 1

print(data)
