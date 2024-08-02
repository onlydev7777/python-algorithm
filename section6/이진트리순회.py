def pre_order(N, depth):
  if depth == 3:
    return
  print(N, end=' ')
  depth += 1
  pre_order(N * 2, depth)
  pre_order(N * 2 + 1, depth)


def in_order(N, depth):
  if depth == 3:
    return
  depth += 1
  in_order(N * 2, depth)
  print(N, end=' ')
  in_order(N * 2 + 1, depth)


def post_order(N, depth):
  if depth == 3:
    return
  depth += 1
  post_order(N * 2, depth)
  post_order(N * 2 + 1, depth)
  print(N, end=' ')


pre_order(1, 0)
print()
in_order(1, 0)
print()
post_order(1, 0)
