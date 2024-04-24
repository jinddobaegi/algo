def dfs(start):
    # 스타트 지점에서 시작해서
    # child 노드를 다 방문해서
    # 제일 긴 경로랑
    # 두번 째로 긴 경로..

    visited = [0]


n = int(input())
parent = [[]*(n+1)]
for _ in range(n-1):
    u, v, w = map(int, input().split())
    parent[u].append((v, w))

max_v = INF
for i in range(n):
    dfs(i)