N, K = map(int, input().split())  # 물품의 수, 버틸 수 있는 무게
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        w = arr[i-1][0]
        v = arr[i-1][1]

        if j < w:  # 물건을 넣을 수 없는 경우
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])  # 넣은 경우, 넣지 않은 경우 중 최댓값

print(dp[N][K])