def solution(lines):
  row = [0] * 201
  for start, end in lines:
    for i in range(start + 100, end + 100):
      row[i] += 1

  return sum(1 for v in row if v > 1)


print(solution([[0, 1], [2, 5], [3, 9]]))
