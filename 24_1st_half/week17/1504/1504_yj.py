import sys
import heapq
input = sys.stdin.readline

N, E = map(int, input().split()) # 정점의 개수, 간선의 개수
arr = [[] for _ in range(N+1)]
INF = int(1e9)

for _ in range(E):
    a, b, c = map(int, input().split())
    # 방향성 없는 그래프
    arr[a].append((b, c))
    arr[b].append((a, c))

def dijkstra(s, e):
    pq = []
    distance = [INF] * (N+1)
    heapq.heappush(pq, (0, s))
    distance[s] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for next, cost in arr[now]:
            new_dist = dist + cost

            if distance[next] > new_dist:
                distance[next] = new_dist
                heapq.heappush(pq, (new_dist, next))

    return distance[e]

v1, v2 = map(int, input().split())  # 반드시 거쳐야 하는 정점
# 경로1 = 1, v1, v2, N / 경로2 = 1, v2, v1, N
p1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
p2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

if p1 >= INF and p2 >= INF:  # 최단 경로가 존재하지 않는 경우
    print(-1)
else:
    print(min(p1, p2))