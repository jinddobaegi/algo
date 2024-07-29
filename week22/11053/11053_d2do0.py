# 가장 긴 증가하는 부분수열
# DP연습문제

N = int(input())
A = list(map(int, input().split()))

dp = [1 for _ in range(N)] # DP 초기화된 배열(?) 최소값은 1

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]: # 오름차순
            dp[i] = max(dp[i], dp[j] + 1) # dp값을 갱신시켜주면서

print(max(dp))