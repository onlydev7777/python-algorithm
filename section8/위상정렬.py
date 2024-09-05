import sys
from collections import deque

sys.stdin = open("위상정렬.txt", "rt")

N, M = map(int, input().split())
degree = [0] * (N + 1)
arr = list()
deq = deque()

for _ in range(M):
  s, e = map(int, input().split())
  arr.append((s, e))
  degree[e] = degree[e] + 1

for i in range(1, N + 1):
  if degree[i] == 0:
    deq.append(i)

while deq:
  s = deq.popleft()
  print(s, end=' ')
  target = [tup for tup in arr if tup[0] == s]
  for v in target:
    degree[v[1]] = degree[v[1]] - 1
    if degree[v[1]] == 0:
      deq.append(v[1])
