import sys
from collections import deque

sys.stdin = open("단어찾기.txt", "rt")

N = int(input())
arr = []
deq2 = deque()

for _ in range(N):
  arr.append(input())

for _ in range(N - 1):
  deq2.append(input())

deq = deque(arr)

for v in arr:
  if v in deq2:
    deq.remove(v)
    deq2.remove(v)

print(deq[0])
