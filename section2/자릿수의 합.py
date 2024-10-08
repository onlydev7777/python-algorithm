# N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고,
# 그 합이 최대인 자연수를 출력 하는 프로그램을 작성하세요.
#
# 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 꼭 작성해서 프로그래밍 하세요.
#
# ▣ 입력설명
# 첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
# 각 자연수의 크기는 10,000,000를 넘지 않는다.
#
# ▣ 출력설명
# 자릿수의 합이 최대인 자연수를 출력한다.
# 자릿수의 합이 같을 경우 입력순으로 먼저인 숫자 를 출력합니다.

import sys


def digit_sum(x):
  sum = 0
  for c in x:
    sum += int(c)
  return sum


sys.stdin = open("자릿수의 합.txt", "rt")

n = int(input())
arr = list(map(str, input().split()))

max = 0
res = 0

for i in arr:
  tot = digit_sum(i)
  if max < tot:
    max = tot
    res = i

print(res)
