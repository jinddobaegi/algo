T = int(input())

for _ in range(T):
    chap = int(input())
    data = list(map(int, input().split()))
    dp = [[0 for i in range(chap + 1)] for j in range(chap + 1)]

    # 연속된 두 수의 합을 2차원 dp배열에 넣어주기
    for i in range(1, chap):
        for j in range(2, chap + 1):
            if i + 1 == j:
                dp[i][j] = data[i] + data[j]

    for i in range(2, chap + 1):
        for j in range(1, chap + 2 - i): # 배열의 시작점
            # 더 작은 값 넣어주기...를 어케 하누

