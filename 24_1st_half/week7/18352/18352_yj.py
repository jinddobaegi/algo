# 100% 다 이해는 못 함ㅠㅠ
import sys
import heapq
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for i in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)  #단방향

# 누적 거리를 계속 저장
INF = int(1e9)
dis = [INF] * (N+1)  # 갈 수 없다면 INF 값을 가지도록

def dijkstra(start):
    # 우선순위 큐
    pq = []
    # 출발점 초기화
    heapq.heappush(pq, (0, start))
    dis[start] = 0

    while pq:
        # 현재 시점에서
        # 누적 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)

        # 이미 방문한 지점 + 누적 거리가 더 짧게 방문한 적이 있다면 pass
        if dis[now] < dist:
            continue

        # 인접 노드 확인
        for j in graph[now]:
            new_cost = dist + 1   # 거리 1 고정

            # 누적 거리가 기존보다 크면
            if dis[j] <= new_cost:
                continue

            dis[j] = new_cost
            heapq.heappush(pq, (new_cost, j))

dijkstra(X)

if K in dis:
    for i in range(1, N+1):
        if dis[i] == K:
            print(i)
else:
    print(-1)