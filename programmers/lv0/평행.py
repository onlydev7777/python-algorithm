def solution(dots):
  slopes = []
  for i in range(4):
    for j in range(i + 1, 4):
      slopes.append(slope(dots[i], dots[j]))
  if slopes[0] == slopes[5] or slopes[1] == slopes[4] or slopes[2] == slopes[3]:
    return 1
  return 0


def slope(p1, p2):
  # x축 차이가 0이 아닌 경우에만 기울기를 구합니다.
  if p2[0] - p1[0] != 0:
    return (p2[1] - p1[1]) / (p2[0] - p1[0])
  else:
    return float('inf')  # 수직인 경우 기울기를 무한대로 처리


print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))
print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))
