N = int(input()) # 좌석 개수
M = int(input()) # 고정석 개수
vip = [int(input()) for _ in range(M)]

def solve(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2
        for i in range(3, n + 1):  # 좌석이 3개 이상일 경우
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

# 고정석이 있을 때
if M:
    result = 1
    start = 1
    for end in vip:
        result *= solve(end - start)
        start = end + 1
    if start != N:
        end = N + 1
        result *= solve(end - start)
# 고정석이 없을 때
else:
    result = solve(N)

print(result)