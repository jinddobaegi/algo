N, M = map(int, input().split())
arr = []
visited = [[0] * M for _ in range(N)]
cnt = 0

for _ in range(N):
    lst = list(input())
    arr.append(lst)

def dfs(i, j):
    global cnt
    if visited[i][j] == 1:
        return

    if arr[i][j] == '-':
        visited[i][j] = 1
        if j + 1 < M and arr[i][j+1] == '-':
            dfs(i, j+1)
        else:
            cnt += 1

    if arr[i][j] == '|':
        visited[i][j] = 1
        if i + 1 < N and arr[i+1][j] == '|' :
            dfs(i+1, j)
        else:
            cnt += 1

for i in range(N):
    for j in range(M):
        dfs(i, j)

print(cnt)