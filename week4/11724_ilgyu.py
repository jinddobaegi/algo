import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
# 여기까진 연결정보 표시해주기

visited = [False] * (n + 1)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)

count = 0
for i in range(1, n + 1):
    if visited[i] == False:
        count += 1
        dfs(i)

print(count)