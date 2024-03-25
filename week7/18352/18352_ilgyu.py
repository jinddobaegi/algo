import heapq
import sys
sys.stdin = open('input.txt')

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist: # 현재 distance에 표시해둔 거리가 내가 while문 돌리면서 뽑은 dist보다 작으면 걔가 최단거리니까
            continue

        for next_node, cost in city[now]:
            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))


N, M, K, X = map(int, input().split())

city = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    city[s].append((e, 1)) # 1은 비용, 이 문제에서는 각 노선마다 비용이 다 똑같아서 그냥 1

# city는 각 노드(도시)로 부터 다른 노드까지 길이 있는지 여부, 있다면 비용이 얼마인지 표시한 리스트
# print(city)
distance = [float('inf')] * (N + 1)
# print(distance)

dijkstra(X)

# print(distance)
# 거리가 정확히 K인 도시들을 찾아서 출력
result = [i for i, dist in enumerate(distance) if dist == K]
# print(result)
if result:
    for city in sorted(result):
        print(city)
else:
    print(-1)
