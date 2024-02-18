N = int(input())
M = int(input())

arr = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0
def dfs(i):
    visited[i] = 1

    for j in arr[i]:
        if visited[j] == 0:
            dfs(j)

for _ in range(M):
    n1, n2 = map(int, input().split())
    arr[n1].append(n2)
    arr[n2].append(n1)

dfs(1)

for i in range(2, N+1):
    if visited[i]:
        cnt += 1

print(cnt)