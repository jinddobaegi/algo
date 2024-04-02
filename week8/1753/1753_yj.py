import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

arr = [[] for i in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    arr[u].append([v, w])

INF = int(1e9)
distance = [INF] * V

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start-1] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now-1] < dist:
            continue

        for next in arr[now]:
            next_node = next[0]
            cost = next[1]

            # next_node 로 가기 위한 누적 거리
            new_dist = dist + cost

            if distance[next_node-1] <= new_dist:
                continue

            distance[next_node-1] = new_dist
            heapq.heappush(pq, (new_dist, next_node))

dijkstra(K)

for i in distance:
    if i == INF:
        print('INF')
    else:
        print(i)