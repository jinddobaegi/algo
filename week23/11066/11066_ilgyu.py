import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    files = [0] + list(map(int, input().split()))
    s = [0] * (n+1)
    for i in range(1, n+1):
        s[i] = s[i-1] + files[i]
    # print(s)

    dp = [[0] * (n+1) for _ in range(n+1)]
    # dp[i][j]는 i번째 파일부터 j번째 파일까지 합하는데 최소 비용
    for i in range(2, n+1): # 부분 파일의 길이
        for j in range(1, n+2-i): # 부분파일의 시작점,
            dp[j][j+i-1] = min([dp[j][j+k] + dp[j+k+1][j+i-1] for k in range(i-1)]) + (s[j+i-1] - s[j-1])
    # for m in dp:
    #     print(m)
    print(dp[1][n])

    # https: // data - make.tistory.com / 402
