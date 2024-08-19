# 플로이드-워셜 알고리즘 ..
# 모든 정점에서 다른 모든 정점까지의 최단 거리를 구할 때 사용
N = int(input())
M = int(input())
INF = int(1e9)
path = [[[] for _ in range(N+1)] for _ in range(N+1)]  # 최단 경로
graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    graph[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, N+1):  # 경유지
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                path[i][j] = path[i][k] + [k] + path[k][j]  # 경로 갱신

# 도시 간의 최소 비용 출력
for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] != INF:
            print(graph[i][j], end = " ")
        else:
            print(0, end = " ")
    print()

# 경로 출력
for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == INF or i == j:
            print(0)
        else:
            print(len(path[i][j]) + 2, i, *path[i][j], j)