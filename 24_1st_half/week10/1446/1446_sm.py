# 지름길
# 실버1

# 문제
# D킬로미터 길이의 고속도로를 지난다.
# 커브가 많
# 세준이는 이 고속도로에 지름길이 존재한다는 것을 알게 되었다.
# 모든 지름길은 일방통행이고, 고속도로를 역주행할 수는 없다.

# 세준이가 운전해야 하는 거리의 최솟값
# 지름길 시작이 도착보다 작다

# 전략
# 다 돌면서 최솟값 찾기


# 입력
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n, d = map(int, input().split())

distance = [INF] * (d + 1)
graph = [[] for _ in range(d + 1)]

for i in range(d):
    graph[i].append((i + 1, 1))

for _ in range(n):
    start, arrive, length = map(int, input().split())

    if arrive > d:
        continue

    # 지름길 정보
    graph[start].append((arrive, length))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            # i[0] 길/지름길 도착지점
            # i[1] 길/지름길 길이
            # 현재 지점
            cost = dist + i[1]  # 현재 지점에서 길/지름길을 더함

            # 해당 노드로 가는데 계산된 비용이 최단거리테이블보다 작으면 업데이트
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(0)
print(distance[d])