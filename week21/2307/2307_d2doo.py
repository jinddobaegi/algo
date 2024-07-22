# 도로검문
# 일단 다익스트라만 구현함 ㅠ

import heapq

def dijkstra(N, roads, start):
    graph = [[] for _ in range(N + 1)]
    for u, v, w in roads:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # 거리 무한대로 초기화
    dist = [float('inf')] * (N + 1)
    dist[start] = 0

    # 우선순위 큐 사용
    pq = [(0, start)]

    while pq:
        now_dist, now_node = heapq.heappop(pq)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if now_dist > dist[now_node]:
            continue

        # 인접 노드 확인
        for next, cost in graph[now_node]:
            distance = now_dist + cost

            # 더 짧은 경로를 발견한 경우
            if distance < dist[next]:
                dist[next] = distance
                heapq.heappush(pq, (distance, next))

    return dist


# 입력 처리
N, M = map(int, input().split())
roads = []
for _ in range(M):
    a, b, t = map(int, input().split()) # 도로 a, 도로 b, 통과시간 t
    roads.append((a, b, t))

# 1번 노드에서 시작하여 N번 노드까지의 최단 시간 구하기
distances = dijkstra(N, roads, 1)
result = distances[N]

