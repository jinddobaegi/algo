# 작업들 선행관계 - 선행 작업들은 번호 다 작음
# 선행 관계 없는 작업도 있음 - 동시에 수행 가능

# 소요 시간, 선행 작업 개수, 선행 작업 번호
# 선행작업 확인하려면 끝에서부터 for문 돌기?
# 선행 관계에 있으면 작업 하나로 보기
N = int(input())
time = [0] * (N+1)
works = [[] for _ in range(N+1)]

for i in range(1, N+1):
    a, b, *c = map(int, input().split())
    time[i] = a
    if b:
        c.sort(reverse=True)
        works[i] = c

dp = [0] * (N+1)
def sol(i):  # i번 작업에 걸리는 시간
    if not dp[i]:
        dp[i] = time[i]
        tmp = 0
        if works[i]:
            for w in works[i]:
                tmp = max(tmp, sol(w))
        dp[i] += tmp
    return dp[i]

max_v = 0
for i in range(N, 0, -1):
    if not dp[i]:
        max_v = max(max_v, sol(i))

print(max_v)