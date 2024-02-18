N = int(input())
arr = []
visited = [[0] * N for _ in range(N)]
ans = ''

for _ in range(N):
    lst = list(map(int, input().split()))
    arr.append(lst)

def dfs(i, j):
    visited[i][j] = 1

    di = [1, 0]
    dj = [0, 1]

    for k in range(2):
        ni, nj = i + di[k] * arr[i][j], j + dj[k] * arr[i][j]

        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            if arr[ni][nj] == -1:
                visited[ni][nj] = 1
                break
            dfs(ni, nj)

dfs(0, 0)

if visited[N-1][N-1] == 1:
    ans = 'HaruHaru'
else:
    ans = 'Hing'

print(ans)