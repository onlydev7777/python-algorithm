import sys

sys.stdin = open("점수계산.txt", "rt")
n = int(input())
arr = list(map(int, input().split()))

res = 0
svc = 0

for i in arr:
  if i == 0:
    svc = 0
  else:
    svc += 1
    res += svc

print(res)
