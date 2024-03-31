# 최소 비용 구하기 2
import heapq

def dijkstra(parent, start):
    q = []
    heapq.heappush(q, (0, start)) # 의존하는 배열 q, (거리, 시작점)
    distance[start] = 0 # 내가 시작점이니까 거리 0으로 리셋

    while q:
        dist, now = heapq.heappop(q) # 알아서 젤 낮은애가 나옴

        if distance[now] < dist: # 최소 비용을 넣는 distance가
            continue # 제일 최소여서 나온 dist 보다 작다면 이미 다녀갔다는 것.

        for child in parent[now]: # 자식노드 돌아버리기
            # 자식 노드 번호, 거리 꺼내주기
            child_node, geori = child

            # 거리 목록에 적힌 자식 노드까지 가는 최소 거리가
            # 지금 꺼내진 최소거리 + 자식노드까지 가는 거리보다 크다면
            if dist + geori < distance[child_node]:
                distance[child_node] = dist + geori # 거리 갱신
                node_lst[child_node] = now # 겪어왔던 노드,, 적어주기
                # 그리고 q에 또 넣어주기.
                heapq.heappush(q, (dist + geori, child_node))

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

parent = [[] for _ in range(n + 1)]
node_lst = [0] * (n + 1)
for _ in range(m):
    # 버스 노선번호 u, 도착지점 v, 비용 w
    u, v, w = map(int, input().split())
    parent[u].append((v, w))

# 출발지점, 도착 지점
start, destination = map(int, input().split())

# 다익스트라 재료
# 1. 무한(?)
INF = 1e8
# 2. 거리 넣을 리스트(최대거리인 무한(?)을 넣어주고 리스트 수+1 만큼 만들기
distance = [INF] * (n + 1)

dijkstra(parent, start)
print(distance[destination])

path = [] # 경로
curr = destination # 목적지부터 다시 시작하기
while curr:
    path.append(curr)
    curr = node_lst[curr] # 자식리스트에 넣었던 부모노드 꺼내기
print(len(path))

# path.reverse()
for i in path[::-1]:
    print(i, end=" ")
