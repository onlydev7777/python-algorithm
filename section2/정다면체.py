# 두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중
# 가장 확률이 높은 숫자를 출력하는 프로그램을 작성하세요.
#
# 정답이 여러 개일 경우 오름차순으로 출력합니다.
#
# ▣ 입력설명
# 첫 번째 줄에는 자연수 N과 M이 주어집니다. N과 M은 4, 6, 8, 12, 20 중의 하나입니다.

# ▣ 출력설명
# 첫 번째 줄에 답을 출력합니다.
#
# ▣ 입력예제
# 4 6
#
# ▣ 출력예제
# 5 6 7

import sys

sys.stdin = open("정다면체.txt", "rt")
n, m = map(int, input().split())

map = dict()

for i in range(1, n + 1):
  for j in range(1, m + 1):
    val = map.get(i + j, 0)
    map[i + j] = val + 1

max = 0
for val in map.values():
  if val > max:
    max = val

for key in map.keys():
  if map[key] == max:
    print(key, end=" ")
