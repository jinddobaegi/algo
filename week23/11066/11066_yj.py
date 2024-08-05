# 어려워 ~~
# https://hseungyeon.tistory.com/313
T = int(input())

for i in range(T):
    k = int(input())
    arr = list(map(int, input().split()))
    # i에서 j까지 합하는데 필요한 최소 비용
    dp = [[0] * k for _ in range(k)]

    for i in range(k-1):
        dp[i][i+1] = arr[i] + arr[i+1]
        # i ~ j의 누적합
        for j in range(i + 2, k):
            dp[i][j] = dp[i][j-1] + arr[j]

    for n in range(2, k):
        for i in range(k - n):
            j = i + n
            costs = [dp[i][x] + dp[x+1][j] for x in range(i, j)]
            dp[i][j] += min(costs)

    print(dp[0][k-1])