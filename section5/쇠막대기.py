import sys

sys.stdin = open("쇠막대기.txt", "rt")

arr = list(map(str, input()))
stack = list()
lastStack = ''
sum = 0
for v in arr:
  if stack and lastStack == '(' and v == ')':
    stack.pop()
    sum += len(stack)
  elif stack and stack[-1] == '(' and v == ')':
    stack.pop()
    sum += 1
  else:
    stack.append(v)
  lastStack = v

print(sum)
