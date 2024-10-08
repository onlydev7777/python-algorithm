# N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열) 이면 YES를 출력하고
# 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다.
#
# 단 회문을 검사할 때 대소문자를 구분하지 않습니다.
#
# ▣ 입력설명
# 첫 줄에 정수 N(1<=N<=20)이 주어지고, 그 다음 줄부터 N개의 단어가 입력된다. 각 단어의 길이는 100을 넘지 않는다.
#
# ▣ 출력설명
# 각 줄에 해당 문자열의 결과를 YES 또는 NO로 출력한다.

import sys

sys.stdin = open("회문문자열 검사.txt", "rt")

n = int(input())

# 1.
# for i in range(n):
#   str = input().lower()
#   rev = str[::-1]
#   if str == rev:
#     print("#%d YES" % (i + 1))
#   else:
#     print("#%d NO" % (i + 1))

# 2.
for i in range(n):
  str = input().lower()
  strLen = len(str)
  for j in range(strLen // 2):
    if str[j] != str[strLen - 1 - j]:
      print("#%d NO" % (i + 1))
      break
  else:
    print("#%d YES" % (i + 1))
