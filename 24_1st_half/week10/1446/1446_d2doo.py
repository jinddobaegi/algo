# 지름길
# 다익스트라
import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next, next_d in graph[now]:
            geori = dist + next_d
            if geori < distance[next]:
                distance[next] = geori
                heapq.heappush(q, (geori, next))

# 지름길 개수 N, 가야하는 거리 D
N, D = map(int, input().split())
graph = [[] for _ in range(D + 1)]
INF = 1e9
distance = [INF] * (D + 1)

# 지름길이 없을 수도 있으니까 모든 노드에 다음 노드까지의 거리를 1로 넣어줌(가야하는 길 더해줘야 함)
for i in range(D):
    graph[i].append((i + 1, 1))

for _ in range(N):
    u, v, w = map(int, input().split())
    if v > D: # 가야하는 거리보다 멀면 무시
        continue
    graph[u].append((v, w))

dijkstra(0)
print(distance[D])