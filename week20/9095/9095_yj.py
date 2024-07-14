# 다음엔 dp로도 풀어보겠습니다 ㅠㅠ
T = int(input())

def dp(N):  # 함수 이름 할만한 게 없어서 dp라고 해버리기..
    if N == 1:
        return 1
    elif N == 2:
        return 2
    elif N == 3:
        return 4
    else:  # N이 3보다 큰 경우
        return dp(N-3) + dp(N-2) + dp(N-1)

for _ in range(T):
    N = int(input())
    print(dp(N))