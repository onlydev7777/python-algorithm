# N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램을 작성하세요.
# 예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력 한다.
# 단 910를 뒤집으면 19로 숫자화 해야 한다.
# 첫 자리부터의 연속된 0은 무시한다.

# 뒤집는 함수인 def reverse(x) 와
# 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성하여 프로그래밍 한다.

# ▣ 입력설명
# 첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
# 각 자연수의 크기는 100,000를 넘지 않는다.

# ▣ 출력설명
# 첫 줄에 뒤집은 소수를 출력합니다. 출력순서는 입력된 순서대로 출력합니다.

import sys

sys.stdin = open("뒤집은 소수.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))


def reverse(num):
  res = ""
  for c in str(num)[::-1]:
    res += c
  return int(res)


def isPrime(num):
  if num == 1:
    return False

  for i in range(2, num // 2 + 1):
    if num % i == 0:
      return False
  return True


for i in arr:
  rev = reverse(i)
  if isPrime(rev):
    print(rev, end=" ")
