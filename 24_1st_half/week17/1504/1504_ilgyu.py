import sys
sys.stdin = open('input.txt')
import heapq

def dijkstra(start, end):
    distance = [200000000 for i in range(N + 1)]
    # print(distance)
    pq = []
    heapq.heappush(pq, (0, start))
    # print(pq)
    while pq:
        dist, cur = heapq.heappop(pq)
        if cur == end:
            return dist
        for next, weight in graph[cur]:
            # print([next, weight])
            if distance[next] <= dist + weight:
                continue
            new_dist = dist + weight
            distance[next] = new_dist
            heapq.heappush(pq, (new_dist, next))
    return -1

N, E = map(int, input().split()) # 정점, 간선수
# a에서 b로 양방향 거리 c
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c]) # 양방향이니까 반대도 표시해줘야함

essential_node = list(map(int, input().split()))
# print(essential_node)

# 1. essentail_node는 반드시 지나야함
# 2. 정점, 간선은 중복돼도 상관 없음  => visited 안 써야 할듯
# 3. 4를 도착점보다는 1에서 각 정점으로 가는 거리를 구하는게 나을 듯

# print(distance)
x = dijkstra(1, essential_node[0])
y = dijkstra(essential_node[0], essential_node[1])
z = dijkstra(essential_node[1], N)

xx = dijkstra(1, essential_node[1])
yy = dijkstra(essential_node[1], essential_node[0])
zz = dijkstra(essential_node[0], N)

ans1 = x + y + z if x != -1 and y != -1 and z != -1 else -1
ans2 = xx + yy + zz if xx != -1 and yy != -1 and zz != -1 else -1

if ans1 == -1 and ans2 == -1:
    print(-1)
# elif 문처럼 각 케이스 전부 처리해줘야함
# 예를 들어 1 - 2 - 3 - 4는 경로가 있는데
# 1 - 3 - 2 - 4 는 경로가 없을 수도 있음
elif ans1 == -1:
    print(ans2)
elif ans2 == -1:
    print(ans1)
else:
    print(min(ans1, ans2))
# 길없는 경우 처리를 단순히 ans1, ans2 둘중 하나라도 길없으면 -1처리 이렇게 하면 안됨

# 반례
# 6 7
# 1 2 2
# 2 3 2
# 3 4 2
# 4 5 2
# 5 6 2
# 1 3 1
# 3 5 1
# 2 5
# 위 케이스 경우 1 - 2 - 5 - 6의 경우 7로 길이 존재하지만
# 1 - 5 - 2 - 6 은 존재하지 않음
# 이런 경우 때문에 둘중 하나라도 길이 존재할 경우를 처리해줘야함



