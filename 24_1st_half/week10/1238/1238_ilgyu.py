import sys
sys.stdin = open('input.txt')
import heapq

def dijkstra(s, e):
    distance = [float('inf')] * (n + 1)
    pq = []
    heapq.heappush(pq, (0, s)) # 가중치, 시작점

    while pq:
        dist, node = heapq.heappop(pq)
        if node == e:
            return dist
        else:
            if distance[node] < dist:
                continue
            for next in graph[node]:
                # print('예비 next_node, new_dist:', next)
                next_node, new_dist = next[0], dist+next[1]
                if distance[next_node] <= new_dist:
                    continue
                else:
                    distance[next_node] = new_dist
                    heapq.heappush(pq, (new_dist, next_node))


n, m, x = map(int, input().split()) # 학생, 단방향 도로, x는 도착점
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, dist = map(int, input().split())
    graph[start].append([end, dist])

# print(graph)


# for m in graph:
#     print(m)
# 갔다 와야함
# 일단 가는거 까지만
# x = dijkstra(4, 2)
# y = dijkstra(2, 4)
# print(x)
# print(y)

ans_list = [0] * (n+1)
for i in range(1, n+1):
    ans1 = dijkstra(i, x) # 가는거
    ans2 = dijkstra(x, i) # 돌아오는거
    ans_list[i] += ans1
    ans_list[i] += ans2
print(max(ans_list))
