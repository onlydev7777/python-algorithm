import sys

sys.stdin = open("재귀함수 이용한 이진수 출력.txt", "rt")


def bin_num(N):
  quot = N // 2
  if quot >= 0:
    if quot > 0:
      bin_num(quot)
    print(N % 2, end='')


N = int(input())

bin_num(N)
