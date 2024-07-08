import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

arr = [[] for i in range(N+1)]

for _ in range(M):
    s, e, c = map(int, input().split())
    arr[s].append([e, c])

INF = int(1e9)
distance = [INF] * (N+1)
path_lst = [0] * (N+1)

A, B = map(int, input().split())

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

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
            path_lst[next_node] = now    # 경로 저장
            heapq.heappush(pq, (new_dist, next_node))

dijkstra(A)

# 도착 도시까지 가는데 드는 최소 비용
print(distance[B])

# 최소 비용 갖는 경로에 포함되어있는 도시의 개수
# 최소 비용 갖는 경로를 방문하는 도시 순서대로 출력
path = []
r = B  # 도착 지점부터 거꾸로 가보자
while r:
    path.append(r)
    r = path_lst[r]  # 루트 출력하기 위해 부모 노드 꺼내옴

print(len(path))
print(' '.join(map(str, path[::-1])))