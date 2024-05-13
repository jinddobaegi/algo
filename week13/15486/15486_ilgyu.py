import sys
sys.stdin = open('input.txt')

N = int(input())
dp = list(0 for _ in range(N + 1))

for now in range(N):
    T, P = map(int, input().split(' '))
    # T = 상담을 완료하는데 필요한 일수
    # P = 해당 상담을 완료했을 때 받을 수 있는 수익

    # 오늘 상담하지 않고 넘어가는 경우 현재까지의 최대 이익을 다음 날로 이월
    dp[now + 1] = max(dp[now + 1], dp[now])

    # 마지막날 안 넘어가면
    if now + T < N + 1:
        dp[now + T] = max(dp[now + T], dp[now] + P)
        # 예제기준
        # 1일에 얻을 수 있는 이익은 작업일3일, 10
        # 3일차에(dp[3]) 얻는 이익은
        # dp[3]과 dp[1]에 첫날에 얻는 이익값 10을 더한 dp[1]+10 둘중 큰 값 비교
        # 왜냐하면 dp리스트 자체가 최대값 담았다고 가정하니까
        # dp[3] = max(dp[3], dp[0] + 1)
print(dp[-1])