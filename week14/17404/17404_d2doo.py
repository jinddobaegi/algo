# from itertools import permutations
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# num = [i for i in range(N)]
# num_per = []
#
# for i in permutations(num):
#     num_per.append(i)
# # print(num_per) # [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
#
# for i in num_per:
#     a, b, c = i

# RBG 2
N = int(input())
INF = 10 ** 6
cost = [list(map(int, input().split())) for _ in range(N)]

answer = INF

# (0: Red, 1: Green, 2: Blue)
for first_color in range(3):
    dp = [[0] * 3 for _ in range(N)]
    dp[0] = [INF, INF, INF] # 무한대로 초기화 하면
    dp[0][first_color] = cost[0][first_color] # 색깔을 넣어준 애 뺴고 다 크니까 안들어가게 됨.

    # DP 배열을 채웁니다
    for i in range(1, N):
        dp[i][0] = cost[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = cost[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = cost[i][2] + min(dp[i - 1][0], dp[i - 1][1])

    for last_color in range(3):
        if last_color != first_color: # 마지막 색상이 다르다면?
            answer = min(answer, dp[N - 1][last_color])

print(answer)
