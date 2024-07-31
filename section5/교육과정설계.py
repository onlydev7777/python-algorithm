import sys
from collections import deque

sys.stdin = open("교육과정설계.txt", "rt")

nes = list(map(str, input()))
N = int(input())

for i in range(N):
  lec = deque(list(map(str, input())))
  nesIdx = 0
  while lec:
    data = lec.popleft()
    if data in nes:
      if nes.index(data) != nesIdx:
        print('#', (i + 1), ': NO')
        break
      elif nes.index(data) == nesIdx:
        nesIdx += 1
  else:
    if nesIdx < len(nes):
      print('#', (i + 1), ': NO')
    else:
      print('#', (i + 1), ': YES')
