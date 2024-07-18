# 오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로그램을 작성하세요.
#
# ▣ 입력설명
# 첫 번째 줄에 첫 번째 리스트의 크기 N(1<=N<=100)이 주어집니다. 두 번째 줄에 N개의 리스트 원소가 오름차순으로 주어집니다.
# 세 번째 줄에 두 번째 리스트의 크기 M(1<=M<=100)이 주어집니다. 네 번째 줄에 M개의 리스트 원소가 오름차순으로 주어집니다.
# 각 리스트의 원소는 int형 변수의 크기를 넘지 않습니다.
#
# ▣ 출력설명
# 오름차순으로 정렬된 리스트를 출력합니다.

import sys

sys.stdin = open("두 리스트 합치기.txt", "rt")

n1 = int(input())
arr1 = list(map(int, input().split()))

n2 = int(input())
arr2 = list(map(int, input().split()))

arr3 = list()

p1 = 0
p2 = 0

while p1 < n1 and p2 < n2:
  if arr1[p1] < arr2[p2]:
    arr3.append(arr1[p1])
    p1 += 1
  else:
    arr3.append(arr2[p2])
    p2 += 1

if p1 == n1:
  arr3 = arr3 + arr2[p1:]
elif p2 == n2:
  arr3 = arr3 + arr1[p2:]

for i in arr3:
  print(i, end=' ')
