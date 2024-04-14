import heapq

N, D = map(int, input().split())   # 지름길의 개수, 고속도로의 길이
arr = [[] for _ in range(D+1)]

INF = int(1e9)
distance = [INF] * (D+1)

for _ in range(N):
    s, e, l = map(int, input().split())
    if e > D:
        continue
    arr[s].append([e, l])

def dijkstra(s):
    pq = []
    heapq.heappush(pq, (0, s))
    distance[s] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for next in arr[now]:
            next_node = next[0]
            cost = next[1]

            new_dist = dist + cost

            if distance[next_node] <= new_dist:
                continue

            distance[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))


for i in range(D):
    arr[i].append((i+1, 1))

dijkstra(0)
print(distance[D])