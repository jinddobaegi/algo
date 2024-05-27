import sys
sys.stdin = open('input.txt')

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*3 for _ in range(N)]

# 첫줄시작색을 정하고 마지막줄은 첫줄과 다른색고르게
# for문을 2줄~ n-1줄까지만 도는겨
# ans_list =[]
# for k in range(3):
#     if k == 0:
#     # 1. R시작
#         dp[0][0] = costs[0][0]
#         dp[0][1] = 1000
#         dp[0][2] = 1000
#
#         for i in range(1, N-1):
#             dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
#             dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
#             dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
#
#         dp[N-1][0] = 3000
#         dp[N-1][1] = min(dp[N-2][0], dp[N-2][2]) + costs[N-1][1]
#         dp[N-1][2] = min(dp[N-2][0], dp[N-2][1]) + costs[N-1][2]
#
#         mylist = dp[N-1]
#         ans = min(dp[N-1])
#         ans_list.append(ans)
#
#     if k == 1:
#         # 2. G시작
#         dp[0][0] = 1000
#         dp[0][1] = costs[0][1]
#         dp[0][2] = 1000
#
#         for i in range(1, N-1):
#             dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
#             dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
#             dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
#
#         dp[N-1][0] = min(dp[N-2][1], dp[N-2][2]) + costs[N-1][0]
#         dp[N-1][1] = 3000
#         dp[N-1][2] = min(dp[N-2][0], dp[N-2][1]) + costs[N-1][2]
#
#         mylist = dp[N - 1]
#         ans = min(dp[N - 1])
#         ans_list.append(ans)
#
#     if k == 2:
#         # 3. B시작
#         dp[0][0] = 1000
#         dp[0][1] = 1000
#         dp[0][2] = costs[0][2]
#
#         for i in range(1, N-1):
#             dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
#             dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
#             dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
#
#         dp[N-1][0] = min(dp[N-2][1], dp[N-2][2]) + costs[N-1][0]
#         dp[N-1][1] = min(dp[N-2][0], dp[N-2][2]) + costs[N-1][1]
#         dp[N-1][2] = 3000
#
#         mylist = dp[N - 1]
#         ans = min(dp[N - 1])
#         ans_list.append(ans)
#
# print(min(ans_list))

# 일반화
ans_list = []
for k in range(3):
    # 3. B시작
    dp[0][0] = float('inf')
    dp[0][1] = float('inf')
    dp[0][2] = float('inf')
    dp[0][k] = costs[0][k]

    for i in range(1, N - 1):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]

    dp[N - 1][0] = min(dp[N - 2][1], dp[N - 2][2]) + costs[N - 1][0]
    dp[N - 1][1] = min(dp[N - 2][0], dp[N - 2][2]) + costs[N - 1][1]
    dp[N - 1][2] = 3000

    dp[N - 1][0] = min(dp[N - 2][1], dp[N - 2][2]) + costs[N - 1][0]
    dp[N - 1][1] = min(dp[N - 2][0], dp[N - 2][2]) + costs[N - 1][1]
    dp[N - 1][2] = min(dp[N - 2][0], dp[N - 2][1]) + costs[N - 1][2]
    dp[N - 1][k] = float('inf')

    mylist = dp[N - 1]
    ans = min(dp[N - 1])
    ans_list.append(ans)
print(min(ans_list))