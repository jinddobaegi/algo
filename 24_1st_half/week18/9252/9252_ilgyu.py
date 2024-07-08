# import sys
# sys.stdin = open('input.txt')
#
#
# word1 = list(map(str, input()))
# word2 = list(map(str, input()))
#
# # 단어는 최대 1000글자
# n = len(word1)
# m = len(word2)
# res = []
# dp = [[] for _ in range(n)]
#
# idx = 0
#
# while idx != n:
#     for i in range(idx, n):
#         for j in range(m):
#             if word1[i] != word2[j]:
#                 continue
#             elif word1[i] == word2[j]:
#                 if i <= j:
#                     res.append(word2[j])
#                     break
#     dp[idx].append([len(res), *res])
#     res = []
#     idx += 1
# # print(max(dp))
# ans = max(dp)
# if ans[0][0] == 0:
#     print(0)
# else:
#     print(ans[0][0])
#     print("".join(map(str, ans[0][1:])))


import sys
sys.stdin = open('input.txt')

# 편의상 맨 앞에 공백추가
word1 = [""] + list(map(str, input()))
word2 = [""] + list(map(str, input()))

# 단어는 최대 1000글자
n = len(word1)
m = len(word2)
# dp[i][j]는 word1의 i번째까지의 문자열과 B의 j번째까지의 문자열의 LCS 길이를 뜻함
dp = [[""] * m for _ in range(n)]
# for m in dp:
#     print(m)

# CAPCAK
# ACAYKP
# 단어1을 행(n)으로
for i in range(1, n): # i =2
    for j in range(1, m): # j = 4
        # dp[1][1] = 없음 , dp[1][2] = C, dp[1][3] = C
        # dp[2][1] = A, dp[2][2] = C,dp[2][3] = 1
        # dp[3][2] = A
        if word1[i] == word2[j]:
            dp[i][j] = dp[i-1][j-1] + word1[i]
            # dp[2][4] = dp[1][3] + C
            # 왜냐면 단어1의 i번째랑 단어2의 j번째가 같으니까
            # 단어1의 i-1번째랑 단어2의 j-1번째에다가 공통된 알파벳만 추가해주면 됨
            # 진짜 단순하게 abc랑 ac가 있다고 하면
            # 마지막 c를 확인하기 전까지는 ab, a가 내가 아는 단어
            # 근데 마지막 c가 같으니까
            # ab, a에서는 공통된게 a뿐이엇는데 abc, ac로 c가 공통되니까
            # ab, a (이게 i-1, j-1까지 확인했을 때 단어)에다가 i, j번째인 c만 추가하면 됨

        else: # 다른경우에는 그냥 이전 dp에서 더 큰애 골라주면 됨
            # 그니까 dp[i][j]로 가는 길이 두갠데 그중 큰 값을 선택하는거
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

res = dp[-1][-1]
print(len(res))
print(res)




