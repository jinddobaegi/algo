# 모든 집을 칠하는 비용의 최솟값 출력
N = int(input())   # 집의 수
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]
dp[0] = arr[0]   # 처음 집을 칠하는 비용은 초기 비용 그대로

# i번 집을 각각 R, G, B로 칠할 때의 최소비용 구하기
for i in range(1, N):
    # ex) R을 칠했을 때, G/B 중 최소 비용 + R 칠하는 비용
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]

ans = min(dp[N-1])
print(ans)