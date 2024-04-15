# 파티
# 다익스트라
import heapq

def dijkstra(start, end):
    q = []
    # 일일이 구해야해서 거리를 함수가 실행될 때 마다 초기화
    distance = [INF] * (N + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0 # 시작지점은 0으로 초기화

    while q:
        d, now = heapq.heappop(q)
        if distance[now] < d: # 이미 다녀감
            continue

        for e, dst in graph[now]: # 도착점, 소요거리 꺼내고
            geori = d + dst # 거리에 지금까지의 최소거리 + 꺼낸 소요거리

            if geori < distance[e]: # 지금까지 기록된 최소거리보다 작으면
                heapq.heappush(q, (geori, e)) # e에서 시작하는 거 다시 시작,,
                distance[e] = geori

    return distance[end] # 최소거리 구한거 반환


# N개의 마을, M개의 단방향 도로, 모이는 마을 X
N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
INF = 1e9

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 최대로 왔다갔다하는 애 찾는거니까 0으로 두고
dist = 0
# 최단 경로 + X 마을에서 각자의 집까지의 최단 경로
for i in range(1, N + 1):
    if i == X: # 해당 마을에 사는 애는 필요가 없당
        continue
    # 단방향이니까 왔다갔다 둘 다 최소거리 구해서 더해줘야 함.
    dist = max(dist, dijkstra(i, X) + dijkstra(X, i))

print(dist)