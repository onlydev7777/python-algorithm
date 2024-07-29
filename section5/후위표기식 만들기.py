import sys

sys.stdin = open("후위표기식 만들기.txt", "rt")

arr = list(map(str, input()))
stack = list()
res = ''

for i, v in enumerate(arr):
  if v.isdecimal():
    res += v
  else:
    if v == '(':
      stack.append(v)
    elif v == '*' or v == '/':
      while stack and (stack[-1] == '*' or stack[-1] == '/'):
        res += stack.pop()
      stack.append(v)
    elif v == '+' or v == '-':
      while stack and stack[-1] != '(':
        res += stack.pop()
      stack.append(v)
    elif v == ')':
      while stack and stack[-1] != '(':
        res += stack.pop()
      stack.pop()

while stack:
  res += stack.pop()

print(res)
