import sys

sys.stdin = open("알파코드.txt", "rt")


def DFS(L, idx):
  global cnt
  if L == len(ch):
    cnt += 1
    for v in res[0:idx]:
      print(v, end='')
    print()
    return
  for i in range(1, 27):
    if i < 10:
      if int(ch[L]) == i:
        res[idx] = code[i]
        DFS(L + 1, idx + 1)
    else:
      if int(''.join(ch[L:L + 2])) == i:
        res[idx] = code[i]
        DFS(L + 2, idx + 1)


ch = list(map(str, input()))
code = list()
code.append(0)
for i in range(26):
  code.append(chr(65 + i))

res = [0] * (len(ch) + 1)
cnt = 0
DFS(0, 0)
print(cnt)
