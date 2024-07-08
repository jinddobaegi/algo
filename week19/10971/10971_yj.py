import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
min_cost = int(1e9)

def dfs(current, cnt, cost):
    global min_cost

    if cnt == N:
        if arr[current][i] != 0:  # 다시 시작 지점으로 이동할 수 있는 경우
            min_cost = min(min_cost, cost + arr[current][i])
        return

    for j in range(N):
        if not visited[j] and arr[current][j] != 0:
            visited[j] = 1
            dfs(j, cnt + 1, cost + arr[current][j])
            visited[j] = 0

# 1번부터 돌아보자
for i in range(N):
    visited[i] = 1
    dfs(i, 1, 0)
    visited[i] = 0

print(min_cost)