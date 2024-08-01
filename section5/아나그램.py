import sys

sys.stdin = open("아나그램.txt", "rt")

arr = list(map(str, input()))
arr2 = list(map(str, input()))

dic = dict()
dic2 = dict()

for v in arr:
  dic[v] = dic.get(v, 0) + 1

for v in arr2:
  dic2[v] = dic2.get(v, 0) + 1

for k, v in dic.items():
  if not (k in dic2.keys()) or v != dic2[k]:
    print("NO")
    break
else:
  print("YES")
