import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1]*N for _ in range(M)]

def sol(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    if x == M-1 and y == N-1:  # 목표 지점에 도달한 경우
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내에 있으면서 높이가 더 낮은 지점이라면
            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] < arr[x][y]:
                dp[x][y] += sol(nx, ny)

    return dp[x][y]

print(sol(0, 0))