import sys

sys.stdin = open("후위식 연산.txt")

arr = list(map(str, input()))
stack = []

for c in arr:
  if c.isdecimal():
    stack.append(int(c))
  else:
    second = stack.pop()
    first = stack.pop()
    if c == '+':
      stack.append(first + second)
    elif c == '-':
      stack.append(first - second)
    elif c == '*':
      stack.append(first * second)
    elif c == '/':
      stack.append(first / second)

print(stack.pop())
