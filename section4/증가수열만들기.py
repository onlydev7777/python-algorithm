import sys

sys.stdin = open("증가수열만들기.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))

last = 0
lst = []
data = ""
lp = 0
rp = N - 1

while lp <= rp:
  if arr[lp] > last:
    lst.append((arr[lp], 'L'))
  if arr[rp] > last:
    lst.append((arr[rp], 'R'))

  if len(lst) == 0:
    break;

  lst.sort()
  last = lst[0][0]
  data += lst[0][1]
  if lst[0][1] == 'L':
    lp += 1
  else:
    rp -= 1
  lst.clear()

print(len(data))
print(data)
