import sys
str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()

dp = [[0 for _ in range(len(str1))] for _ in range(len(str2))]

answer = 0
for i in range(len(str2)):
    for j in range(len(str1)):
        if str1[j] == str2[i]:
            # 시작점에 위치할때
            if i == 0 or j == 0:
                dp[i][j] = 1
            # 1씩 더해주면됨
            else:
                dp[i][j] = dp[i - 1][j - 1] + 1
                answer = max(answer, dp[i][j])
        else:
            dp[i][j] = 0

print(answer)


# str1 = input()
# str2 = input()
#
# cnt = 0
# result = 0
# for i in range(len(str1)):
#     for j in range(len(str2)):
#         # 처음 같은 시점이 있다면 그 때부터 탐색
#         if str1[i] == str2[j]:
#             s1, s2 = i, j
#             # 혹시나 범위가 벗어나지 않게
#             while s1 < len(str1) and s2 < len(str2):
#                 if str1[s1] == str2[s2]:
#                     cnt += 1
#                     s1 += 1
#                     s2 += 1
#                 else:
#                     if result < cnt:
#                         result = cnt
#                     cnt = 0
#                     break
#                 # 끝가지 같아서 else를 못들어가는 경우 처리
#                 if s1 == len(str1) or s2 == len(str2):
#                     if result < cnt:
#                         result = cnt
#                     cnt = 0
#                     break
#
# print(result)