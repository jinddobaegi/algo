

# # 2. 2차원 접근
# # dp[i][w] = 최대무게가 w인 가방에서 i번째 물건까지 판단했을 때의 최대 가치
# dp[k+1][w] = dp[k][w]
import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
items = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0] * (k+1) for _ in range(n+1)]
# dp[i][j] = 가방에 j무게까지 담을 수 있을 때, i번째 물건까지 확인했을 때 담을 수 있는 최대 무게

# print(items)
for i in range(1, n+1):
    for j in range(1, k+1):
        weight = items[i][0]
        value = items[i][1]

        if j < weight: # 만약 현재 수용가능 무게보다 물건무게가 더 크면 못담으니까
            dp[i][j] = dp[i-1][j] # 그냥 이전 dp값 그대로
        else: # 담을 수 있으면?
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
            # 예를들어 dp[3][6]의 경우
            # 용량 6인 배낭에 i=3번째 물건(무게3)을 넣을 떄 dp값은
            # dp[2][6-3] + v[3]
            # 즉 넣는다는 가정하에 6에서 3만큼을 빼주면 넣기전의 무게
            # dp[3][6] = dp[2][3]+ w[3]이거랑 안 담는거랑 최대값

print(dp[n][k])
# https://chanhuiseok.github.io/posts/improve-6/
# 2157번이랑 비슷함
