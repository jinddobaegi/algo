import sys
sys.stdin = open("week14/1149/1149.txt")
input = sys.stdin.readline

# 다이나믹 알고리즘은 앞에서 계산한 값을 저장해두고 다음 계산에 사용한다.

house = int(input())
cost = []
for _ in range(house):
    cost.append(list(map(int, input().split()))) # 2차원 배열 생성

# print("cost=", cost)
dp = [[0]*3 for _ in range(house)] # 2차원 배열 생성
dp[0] = cost[0] # 첫번째 집은 그대로 넣어준다.

for i in range(1, house): # 1부터 집의 개수만큼 반복한다.
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0] # 빨간색0 으로 시작 / 이전 집의 초록색1, 파란색2 중 작은 값과 현재 집의 빨간색을 더한다.
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1] # 초록색1 으로 시작
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2] # 파란색2 으로 시작
# 이렇게 계산하면 경우의 수의 모든 값이 저장된다.
# 그중 마지막 집의 값에서 가장 작은 값을 찾는다.

# print("dp =", dp)
print(min(dp[house-1]))







  





  




