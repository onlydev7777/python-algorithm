import sys

sys.stdin = open("가장큰수.txt", "rt")

N, M = map(int, input().split())

arr = list(map(int, str(N)))
stack = list()

for v in arr:
  while stack and M > 0 and stack[-1] < v:
    stack.pop()
    M -= 1
  stack.append(v)

if M != 0:
  stack = stack[:M]

res = ''.join(map(str, stack))
print(res)
