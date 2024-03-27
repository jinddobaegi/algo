#최단경로

# 방향그래프가 주어지면
# 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오.
# 단, 모든 간선의 가중치는 10 이하의 자연수이다.
import heapq

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start)) # 우선순위, 값 형태로 들어감
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq) # 우선순위가 가장 낮은 값이 나옴

        if distance[now] < dist:
            continue

        for child in parent[now]: # 현재 있는 노드의 자식 노드들이 나옴
            child_node, geori = child
            if dist + geori < distance[child_node]:
                distance[child_node] = dist + geori
                heapq.heappush(pq, (dist + geori, child_node))

V, E = map(int, input().split()) # 정점, 간선
K = int(input()) # 루트노드
INF = 1e8

# 부모 노드의 인덱스 번호를 가지고 있는 리스트에 (자식 노드, 간선의 길이) 넣어줄거임
parent = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    parent[u].append((v, w))

dijkstra(K)

for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])