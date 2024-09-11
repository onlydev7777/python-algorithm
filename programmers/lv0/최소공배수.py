def solution(n):
  pizza = 6
  return abs(n * pizza) // gcd(n, pizza) // pizza


def gcd(a, b):
  while b != 0:
    a, b = b, a % b
  return a


print(solution(6))
print(solution(10))
print(solution(4))
