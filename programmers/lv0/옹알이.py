def solution(babbling):
  arr = ["aya", "ye", "woo", "ma"]
  cnt = 0
  for v in babbling:
    vlen = len(v)
    alen = 0
    vtxt = ""
    for vv in v:
      vtxt += vv
      for vvv in arr:
        if vtxt == vvv:
          alen += len(vtxt)
          vtxt = ""
    if vlen == alen:
      cnt += 1
  return cnt


print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))
