import sys
sys.stdin = open('input.txt')
import heapq

def dijkstra(s):
    pq = []
    heapq.heappush(pq, (0, s)) # pq에 0(누적가중치, 시작이니까 0),  s (노드) 저장
    distance[s] = 0

    while pq:
        dist, node = heapq.heappop(pq) # 시작시점엔 0, s

        for next_node, weight in graph[node]: # u, v, w 저장할 때 v, w가 next_node, weight 임 /
            # 이 for문의 의미는 내가 현재(s)에서 다음에 갈 노드와 거기까지의 거리
            # 왜냐면 그래프에 그렇게 저장해놨으니까 (v, w)
            next_dist = dist + weight # 함수 안에서 저장할 떈 (누적 가중치, 노드) 순서지만, 아래서 graph만들땐 (노드, 가중치)순

            if distance[next_node] <= next_dist: # 기록된 가중치가 현재 검사중인 새로운 누적가중치보다 적으면
                continue # 어차피 현재 기록된 값이 더 작으니까 그냥 넘어감

            distance[next_node] = next_dist # 위 if문이 만족하지 않으면 값 새로 갱신해주고
            heapq.heappush(pq, (next_dist, next_node))

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
distance = [float('inf')] * (V+1)
# print(graph)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w]) # 그래프의 인덱스 1번 리스트는 => 1번에서 갈 수 있는 노드와 거기까지의 거리(값) 을 저장
# print(graph)
dijkstra(2)
# print(distance)

for i in range(1, V+1):
    if distance[i] == float('inf'):
        print('INF')
    else:
        print(distance[i])

# 근데 이 문제는 무조건 1번에서 시작한다고 가정하는건가?
# ㄴㄴ 2번 넣으면 그냥 거기부터 시작으로 값 나옴