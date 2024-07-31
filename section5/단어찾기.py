import sys

sys.stdin = open("단어찾기.txt", "rt")

N = int(input())

# -- 2개의 리스트를 사용해서 풀기 --
# arr = []
# deq2 = deque()
#
# for _ in range(N):
#   arr.append(input())
#
# for _ in range(N - 1):
#   deq2.append(input())
#
# deq = deque(arr)
#
# for v in arr:
#   if v in deq2:
#     deq.remove(v)
#     deq2.remove(v)
#
# print(deq[0])

# --dictionary 사용해서 풀기--

d = dict()

for _ in range(N):
  word = input()
  d[word] = d.get(word, 0) + 1

for _ in range(N - 1):
  word = input()
  d[word] = d.get(word, 0) - 1

for key, val in d.items():
  if val == 1:
    print(key)
    break
