import sys

sys.stdin = open("격자판 회문수.txt", "rt")

arr = [list(map(int, input().split())) for _ in range(7)]


def check(c1):
  if c1 == c1[::-1]:
    return True
  else:
    return False


cnt = 0

for i in range(7):
  for j in range(3):
    c1 = ""
    c2 = ""
    for k in range(5):
      c1 += str(arr[i][j + k])
      c2 += str(arr[j + k][i])

    if check(c1):
      cnt += 1
    if check(c2):
      cnt += 1

print(cnt)
