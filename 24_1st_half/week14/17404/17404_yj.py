# 모든 집을 칠하는 비용의 최솟값 출력
# 마지막 집과 첫 번째 집 색 달라야 함

N = int(input())   # 집의 수
arr = [list(map(int, input().split())) for _ in range(N)]
ans = INF = 1e9   # 최솟값을 구하기 위해 초기값을 큰 값으로 설정

for i in range(3):
    dp = [[INF] * 3 for _ in range(N)]
    dp[0][i] = arr[0][i]  # 첫 번째 집의 색상을 고정

    for j in range(1, N):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + arr[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + arr[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + arr[j][2]

    for k in range(3):
        if i != k:   # 처음 집과 마지막 집이 다르면 최솟값 갱신
            ans = min(ans, dp[-1][k])

print(ans)