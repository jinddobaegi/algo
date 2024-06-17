# 특정한 최단경로
# 75% 틀렸습니다.
import heapq
import sys

# 다이끄스뜨라
def dijkstra(start, N, graph):
    distance = [sys.maxsize] * (N + 1) # 갔던 길 또 갈 수 있음(첫빠따에 초기화)
    q = []
    heapq.heappush(q, (0, start)) # 거리, 노드
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q) # 가장 작은 값이 나옴(우선순위가 낮은 값)

        # 이미 적혀있는 값이 더 작으면 재껴
        if distance[node] < dist:
            continue

        for child_node, d in graph[node]:
            cost = dist + d

            # 만약 cost가 다음 노드에 기록되어있는 값보다 작으면
            if distance[child_node] > cost:
                distance[child_node] = cost
                heapq.heappush(q, (cost, child_node))
    return distance

N, E = map(int, input().split()) # 정점 N, 간선 E
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split()) # a번부터 b번까지 양방향
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split()) # 반드시 거쳐야하는 두 친구

# 1 -> v1 -> v2 -> N, 1 -> v2 -> v1 -> N
d1 = dijkstra(1, N, graph)
d2 = dijkstra(v1, N, graph)
d3 = dijkstra(v2, N, graph)
ans = min(d1[v2] + d2[N] + d3[v1], d1[v1] + d2[v2] + d3[N])

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)