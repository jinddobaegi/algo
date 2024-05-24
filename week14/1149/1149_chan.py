import sys
sys.stdin = open("week14/1149/1149.txt")
input = sys.stdin.readline
import queue

#집의수 빨초파비용 모든집을 칠하는 최소비용 
#색상 연속 불가능
# 3
# 26 40 83
# 49 60 57
# 13 89 99

house = int(input())
cost = []
for _ in range(house):
    cost.append(list(map(int, input().split())))
dp = [[0]*3 for _ in range(house)]
dp[0] = cost[0]
print(dp)

for i in range(1, house):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]


print(dp)
print(min(dp[house-1]))






  





  




