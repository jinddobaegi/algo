from sys import stdin

input = stdin.readline

# python3으로 시간초과, pypy로 되길래
# python3으로 엄청 빠른 코드를 보니
# 크누스 최적화 알고리즘이라는 게 있더라...
# https://blog.naver.com/hands731/221809365746

T = int(input())
INF = int(1e9)
for _ in range(T):
    K = int(input())
    arr = [0] + list(map(int, input().split()))
    dp = [[0] * (K+1) for _ in range(K+1)]
    cumsum = [0] * (K+1)
    for i in range(1, K+1):
        cumsum[i] = cumsum[i-1] + arr[i]  # 누적합 배열 만드는 코드

    '''
    s,e가
    12 23 34
    13 24
    14
    순으로 진행돼야 함
    '''
    
    for gap in range(1, K):  # 간격: 1 ~ K-1
        for s in range(1, K - gap + 1):
            e = s + gap
            min_v = INF
            for p in range(s, e):
                min_v = min(min_v, dp[s][p] + dp[p+1][e])
            dp[s][e] = min_v + (cumsum[e] - cumsum[s-1])

    print(dp[1][K])