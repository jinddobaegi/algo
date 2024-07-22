import heapq

N, M = map(int, input().split())  # 지점의 수, 도로의 수
arr = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, t = map(int, input().split())
    arr[a].append((b, t))
    arr[b].append((a, t))

INF = int(1e9)

# 최소 경로 구하는 함수
def dijkstra1(s):
    pq = []
    distance = [INF] * (N + 1)
    route = [-1] * (N + 1)
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
                route[next] = now
                heapq.heappush(pq, (new_dist, next))

    return distance, route

# 검문소 하나씩 세워보면서 계산하는 함수
def dijkstra2(s, r1, r2):
    pq = []
    distance = [INF] * (N + 1)
    heapq.heappush(pq, (0, s))
    distance[s] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for next, cost in arr[now]:
            if (now == r1 and next == r2) or (now == r2 and next == r1):
                continue

            new_dist = dist + cost

            if distance[next] > new_dist:
                distance[next] = new_dist
                heapq.heappush(pq, (new_dist, next))

    return distance

distance, route = dijkstra1(1)
time = distance[N]