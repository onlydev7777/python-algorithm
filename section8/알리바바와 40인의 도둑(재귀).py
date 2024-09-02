import sys

sys.stdin = open("알리바바와 40인의 도둑.txt", "rt")


def DFS(x, y):
  if dyArr[x][y] != 0:
    return dyArr[x][y]
  if x == 0 and y == 0:
    return arr[0][0]
  if y == 0:
    dyArr[x][y] = DFS(x - 1, y) + arr[x][y]
  if x == 0:
    dyArr[x][y] = DFS(x, y - 1) + arr[x][y]
  else:
    dyArr[x][y] = min(DFS(x - 1, y), DFS(x, y - 1)) + arr[x][y]

  return dyArr[x][y]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dyArr = [[0] * N for _ in range(N)]

print(DFS(N - 1, N - 1))
