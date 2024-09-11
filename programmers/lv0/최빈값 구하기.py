def solution(array):
  d = {k: 0 for k in array}
  for k in array:
    d[k] += 1
  maxx = max(d.values())
  cnt = 0
  result = 0
  for k in d.keys():
    if d[k] == maxx:
      cnt += 1
      result = k
  return result if cnt == 1 else -1


# print(solution([1, 2, 3, 3, 3, 4]))
print(7 // 7)
print(1 // 7)
print(15 // 7)
