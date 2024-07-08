import sys
import heapq

def dijkstra(s):
    distance = [float('inf')] * (N+1)
    distance[s] = 0
    q = []
    # heap에 (가중치, 노드) 형식
    heapq.heappush(q, (0, s))
    while q:
        # 최소힙이므로 가중치가 가장 작은 값이 pop
        dist, now = heapq.heappop(q)
        # 이미 최솟값 구했는지 확인
        if distance[now] >= dist:
            # 연결된 노드들 확인
            for v, val in city[now]:
                # 가중치가 더 작은 값이면
                if dist + val < distance[v]:
                    # 갱신
                    distance[v] = dist + val
                    heapq.heappush(q, (dist + val, v))
    return distance

N, M, X = map(int, input().split())
city = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    city[a].append([b, t])
ans = dijkstra(X)
ans[0] = 0
for i in range(1, N+1):
    if i != X:
        res = dijkstra(i)
        ans[i] += res[X]

print(max(ans))