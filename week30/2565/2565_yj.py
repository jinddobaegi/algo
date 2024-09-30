# A-B 전깃줄 연결 -> 교차하는 전깃줄 없어야 함
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
dp = [1] * N

for i in range(N):  # 현재 고려하는 전깃줄 i
    for j in range(i):  # 그 앞 순서인 전깃줄 j
        if arr[j][1] < arr[i][1]:  # i번 전깃줄 B전봇대 값이 크다면, 교차하지 않으므로
            dp[i] = max(dp[i], dp[j]+1)  # dp[j]에 i번 전깃줄을 포함한 값과 비교하여 갱신

print(N-max(dp))