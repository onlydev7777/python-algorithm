def solution(common):
  diff1 = common[1] - common[0]
  diff2 = common[2] - common[1]
  last = common.pop()
  if diff1 == diff2:
    next = last + diff1
  else:
    diff1 = common[1] // common[0]
    next = last * diff1
  return next


print(solution([1, 2, 3, 4]))
print(solution([2, 4, 8]))
