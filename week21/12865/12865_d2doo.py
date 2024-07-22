# 평범한 배낭
# 조합이나 순열로 못푸나!?
# 엥 이해못함

def knapsack(N, K, items):
    # dp[i][j] : i번째 물건까지 고려했을 때 무게 j 이하의 최대 가치
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        weight, value = items[i - 1]
        for j in range(K + 1):
            if j < weight:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

    return dp[N][K]

N, K = map(int, input().split())

items = [tuple(map(int, input().split())) for _ in range(N)]

print(knapsack(N, K, items))