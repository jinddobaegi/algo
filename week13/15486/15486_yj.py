# DP?!
import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)  # 최대 수익 저장

for i in range(N):
    T, P = map(int, input().split())   # 상담 완료하는데 걸리는 기간, 받는 금액

    dp[i+1] = max(dp[i+1], dp[i])   # 현재까지의 최대 이익 & 이전 최대 이익 비교
    if i + T <= N:   # 퇴사 날짜 전이면
        dp[i+T] = max(dp[i+T], dp[i]+P)   # 해당 상담 진행 안할 때 & 해당 상담 진행 시 이익 비교

print(dp[-1])