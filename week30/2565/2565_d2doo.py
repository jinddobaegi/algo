# 전깃줄
# DP

N = int(input())
connect = [list(map(int, input().split())) for _ in range(N)]
connect.sort()
dp = [1] * N

for i in range(1, N): # 비교할 값
    for j in range(0, i): # 비교할 값의 앞 친구들
        if connect[j][1] < connect[i][1]: # 꼬여있지 않으면?
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))