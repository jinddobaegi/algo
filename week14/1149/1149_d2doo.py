# RGB 거리
# DP
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*3 for _ in range(N)]
# print(f'dp = {dp}')
dp[0] = arr[0] # 첫번째 dp줄은 [26, 40, 83]으로 초기화

for i in range(1, N): # 누적으로 합해주기
    dp[i][0] = arr[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = arr[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = arr[i][2] + min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[N-1])) # 제일 마지막 줄에서 제일 작은 수