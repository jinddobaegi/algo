import sys
sys.stdin = open("week13/15486/15486.txt")
input = sys.stdin.readline

# 퇴사? 입사도 어려운데
# 기간동안 얻을 수 있는 최대 수익
# N+1일에 퇴사/ N일 만큼 일할 수 있음

# dp[i] = i일까지 일했을 때 얻을 수 있는 최대 수익

N = int(input())
dp = [0] * (N + 1)
for i in range(N):
    time, pay = map(int, input().split())
    
    if i + time <= N:
        dp[i + time] = max(dp[i + time], dp[i] + pay)
        # print(dp, "time",dp[i + time],"pay",dp[i] + pay ) 

print(max(dp))


