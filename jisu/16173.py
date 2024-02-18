def dfs(x,y):
    visited[x][y] = 1
    dx = [arr[x][y], 0]
    dy = [0, arr[x][y]]
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
            dfs(nx,ny)

    if visited[N - 1][N - 1] == 1:
        return 'HaruHaru'
    else:
        return 'Hing'

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

print(dfs(0, 0))