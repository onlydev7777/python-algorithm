import sys

sys.stdin = open("회의실배정.txt", "rt")

N = int(input())
arr = []
for _ in range(N):
  s, e = map(int, input().split())
  arr.append((s, e))

arr.sort(key=lambda v: (v[1], v[0]))

et = 0
cnt = 0
for s, e in arr:
  if s >= et:
    et = e
    cnt += 1

print(cnt)
