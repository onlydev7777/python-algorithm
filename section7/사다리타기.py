import sys


def DFS(px, py, res):
  if arr[px][py] == 2:
    print(res)
    # sys.exit(-1)
    return
  if px == 9:
    return

  downFlag = True
  for ii in range(2):
    x = px + dx[ii]
    y = py + dy[ii]
    if 0 <= x < 10 and 0 <= y < 10 and arr[x][y] != 0 and ch[x][y] == 0:
      downFlag = False
      break

  if downFlag == False:
    ch[x][y] = 1
    DFS(x, y, res)
    ch[x][y] = 0
  else:
    ch[px + 1][py] = 1
    DFS(px + 1, py, res)
    ch[px + 1][py] = 0


def DFS2(px, py):
  ch[px][py] = 1  # 1개의 경로만 탐색 하기 때문에 ch = 0 으로 처리 할 필요 없음
  if px == 0:
    print(py)
    return

  upFlag = True
  for ii in range(2):
    x = px + dx[ii]
    y = py + dy[ii]
    if 0 <= x < 10 and 0 <= y < 10 and arr[x][y] != 0 and ch[x][y] == 0:
      upFlag = False
      break

  if upFlag == False:
    DFS2(x, y)
  else:
    DFS2(px - 1, py)


sys.stdin = open("사다리타기.txt", "rt")

arr = [list(map(int, input().split())) for _ in range(10)]
ch = [[0] * 10 for _ in range(10)]
dx = [0, 0]
dy = [1, -1]

for i in range(10):
  if arr[0][i] == 1:
    DFS(0, i, i)

for i in range(10):
  if arr[9][i] == 2:
    DFS2(9, i)
    break
