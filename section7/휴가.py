import sys

sys.stdin = open("휴가.txt", "rt")


def DFS(S, summ):
  global maxx
  if maxx < summ:
    maxx = summ
  for i in range(S, N + 1):
    if ch[i] == 0:
      for j in range(i, i + day[i]):
        ch[j] = 1
      if ch[N + 1] == 0:  # 마지막 일자 이후 유효성 검증
        DFS(i + 1, summ + salary[i])
      for j in range(i, i + day[i]):
        ch[j] = 0


def DFS2(L, summ):
  global maxx
  if L == N + 1:
    if maxx < summ:
      maxx = summ
  else:
    if L + day[L] <= N + 1:
      DFS2(L + day[L], summ + salary[L])
    DFS2(L + 1, summ)


N = int(input())
day = [0] * (N + 1)
salary = [0] * (N + 1)

for i in range(1, N + 1):
  a, b = map(int, input().split())
  day[i] = a
  salary[i] = b

ch = [0] * (N * 2)
maxx = 0
DFS(1, 0)
print(maxx)
maxx = 0
DFS2(1, 0)
print(maxx)
