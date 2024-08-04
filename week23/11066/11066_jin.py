from sys import stdin

input = stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    arr = [0] + list(map(int, input().split()))
    cumsum = [0] * (K+1)
    for i in range(1, K+1):
        cumsum[i] = cumsum[i-1] + arr[i]

    dp = [[int(1e9)] * (K+1) for _ in range(K+1)]  # min으로 갱신 위해 큰 수로 init
    for i in range(1, K+1):
        dp[i][i] = 0  # 한 페이지는 합치지 않기 때문에 비용이 0
    
    '''
    ij가
    12 23 34
    13 24
    14
    순으로 진행돼야 함
    '''
    
    for gap in range(1, K):  # 간격: 1 ~ K-1
        for s in range(1, K):  # 시작점: 1 ~ K-1
            e = s + gap
            if e > K:
                break
            # dp[s][e]를 구하기 위해서는
            # 여기서 중간 지점 p를 s~e까지 돌리면서
            # dp[s][p-1]과 dp[p][e]의 합의 최솟값에
            # s~e까지 누적합을 더해줘야 한다
            cumsum_v = cumsum[e] - cumsum[s-1]
            for p in range(s, e):
                dp[s][e] = min(dp[s][e], dp[s][p] + dp[p+1][e] + cumsum_v)

    print(dp[1][K])