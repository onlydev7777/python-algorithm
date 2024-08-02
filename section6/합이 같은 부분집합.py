import sys

sys.stdin = open("합이 같은 부분집합.txt", "rt")


def subset(idx, sum):
  if sum > total // 2:
    return
  if idx == N:
    if sum == total - sum:
      print("YES")
      sys.exit(0)
  else:
    subset(idx + 1, sum + arr[idx])
    subset(idx + 1, sum)


N = int(input())
arr = list(map(int, input().split()))
total = sum(arr)

subset(0, 0)
print("NO")
