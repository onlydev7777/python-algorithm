def solution(numer1, denom1, numer2, denom2):
  denom = denom1 * denom2
  numer = numer1 * denom2 + numer2 * denom1

  temp = gcd(denom, numer)
  answer = [int(numer / temp), int(denom / temp)]
  return answer


def gcd(a, b):
  while b != 0:
    a, b = b, a % b
  return a


print(solution(1, 2, 3, 4))
