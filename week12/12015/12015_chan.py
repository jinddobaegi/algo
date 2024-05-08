import sys
sys.stdin = open('week12/12015/12015.txt')
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [0] * N
dp[0] = 1

for i in range(1, N):
    dp[i] = 1
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))



