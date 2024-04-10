import heapq

N, M, X = map(int, input().split())
arr = [[] for _ in range(N+1)]
time = []

for _ in range(M):
    s, e, t = map(int, input().split())
    arr[s].append([e, t])

INF = int(1e9)

def dijkstra(s, e):
    pq = []
    distance = [INF] * (N+1)   # 학생마다 구하는 것이기 때문에 초기화 시켜줘야 함
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

    return distance[e]  # 도착 지점까지의 최단 거리

# 오고 가는 데 걸리는 시간을 구해야 함
# 각자 집에서 X 마을까지 가는 데 걸리는 최단 시간 + 반대로 집 올 때 최단 시간 더함
for i in range(1, N+1):
    party = dijkstra(i, X)
    home = dijkstra(X, i)
    time.append(party + home)

print(max(time))