import sys

sys.stdin = open("경로탐색.txt", "rt")


# def DFS(L, row):
#   global cnt
#   if L == N:
#     return
#   if arr[row][N] == 1:
#     path.append(N)
#     cnt += 1
#     for v in path:
#       print(v, end=' ')
#     print()
#     path.pop()
#   for i in range(1, N + 1):
#     if ch[i] == 1:
#       continue
#     if arr[row][i] == 1:
#       ch[row] = 1
#       path.append(i)
#       DFS(L + 1, i)
#       path.pop()
#       ch[row] = 0

def DFS(V):
  global cnt
  if V == N:
    cnt += 1
    for v in path:
      print(v, end=' ')
    print()
    return

  for i in range(1, N + 1):
    if arr[V][i] == 1 and ch[i] == 0:
      path.append(i)
      ch[i] = 1
      DFS(i)
      path.pop()
      ch[i] = 0


N, M = map(int, input().split())
arr = [[0] * (N + 1) for _ in range(N + 1)]
ch = [0] * (N + 1)
path = []

for _ in range(M):
  row, col = map(int, input().split())
  arr[row][col] = 1

cnt = 0
ch[1] = 1
path.append(1)
# DFS(1, 1)
DFS(1)
print(cnt)
