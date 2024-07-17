import sys

sys.stdin = open("주사위게임.txt", "rt")

n = int(input())
money = 0
max = 0

for i in range(n):
  arr = input().split()
  arr.sort()
  first, second, third = map(int, arr)

  if first == second and first == third:
    money = 10000 + (first * 1000)
  elif first == second or first == third:
    money = 1000 + (first * 100)
  elif second == third:
    money = 1000 + (second * 100)
  else:
    money = third * 100

  if money > max:
    max = money

print(max)
