import sys
from collections import deque

sys.stdin = open("송아지 찾기.txt", "rt")
S, E = map(int, input().split())

# 1차원 거리 배열 방식
res = 214860000
MAX = 10000
dis = [0] * MAX
dq = deque()
dq.append(S)
while dq:
  now = dq.popleft()
  if now == E:
    break
  for next in (now - 1, now + 1, now + 5):
    if 0 < next <= MAX:
      if dis[next] == 0:
        dq.append(next)
        dis[next] = dis[now] + 1

print(dis[now])
