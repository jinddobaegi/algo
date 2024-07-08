# 비트마스킹 + dp.. 너무 어려워
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1 for _ in range(1 << N)] for _ in range(N)]
inf = int(1e9)

def dfs(current, visited):
    global min_cost

    if visited == (1 << N) - 1:  # 모든 도시를 방문한 경우
        if arr[current][0] == 0:
            return min_cost
        dp[current][visited] = arr[current][0]
        return arr[current][0]

    if dp[current][visited] != -1:
        return dp[current][visited]

    min_cost = inf
    for i in range(N):
        if not visited & (1<<i) and arr[current][i] != 0:  # 방문하지 않았으며 갈 수 있는 경우
            min_cost = min(min_cost, arr[current][i] + dfs(i, visited | (1 << i)))  # 최소 비용 갱신

    dp[current][visited] = min_cost
    return min_cost

print(dfs(0, 1))