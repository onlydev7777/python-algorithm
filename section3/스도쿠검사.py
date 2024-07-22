import sys

sys.stdin = open("스도쿠검사.txt", "rt")

arr = [list(map(int, input().split())) for _ in range(9)]


def check(arr):
  rowSet = set()
  colSet = set()
  rectangleSet = set()

  for i in range(9):
    for j in range(9):
      rowSet.add(arr[i][j])
      colSet.add(arr[j][i])
      if i % 3 == 0 and j % 3 == 0:
        for ii in range(3):
          for jj in range(3):
            rectangleSet.add(arr[i + ii][j + jj])
        if len(rectangleSet) != 9:
          return False
        rectangleSet.clear()

    if len(rowSet) != 9 or len(colSet) != 9:
      return False

    rowSet.clear()
    colSet.clear()

  return True


if check(arr):
  print("YES")
else:
  print("NO")
