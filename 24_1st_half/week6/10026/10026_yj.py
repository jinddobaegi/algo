import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnt = 0
g_cnt = 0

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def dfs(i, j):
    visited[i][j] = 1

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            # 색이 같으면 dfs
            if arr[ni][nj] == arr[i][j]:
                dfs(ni, nj)

# 적록색약이 아닌 사람
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i, j)
            cnt += 1

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

# 적록색약인 사람
visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i, j)
            g_cnt += 1

print(cnt, g_cnt)