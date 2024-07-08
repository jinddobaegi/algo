import sys
sys.stdin = open('input.txt')

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
# print(cost)
min_value = 3000

# 누적합 얼마인지
# dp는 N*N이 아님 !! N*3임 이게 포인트
dp = [[0] * 3 for _ in range(N)]
# print(dp)

# 초기값 설정
dp[0][0] = costs[0][0]
dp[0][1] = costs[0][1]
dp[0][2] = costs[0][2]

# 둘째줄부터 dp
for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

# print(dp)
ans_list = dp[N-1]
ans = min(ans_list)
print(ans)




