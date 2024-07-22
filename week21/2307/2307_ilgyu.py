import sys
sys.stdin = open('input.txt')
import heapq

def find_shortest(s):
    pq = []
    heapq.heappush(pq, (0, s))
    distance = [float('inf')] * (n + 1)
    while pq:
        dist, node = heapq.heappop(pq)
        if distance[node] < dist:
            continue
        for next_node, weight in graph[node]:
            new_dist = dist + weight
            if distance[next_node] < new_dist:
                continue
            distance[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))
            block.append([node, next_node])
    return distance[-1]

def sol(s, x, y):
    pq = []
    heapq.heappush(pq, (0, s))
    ans = [float('inf')] * (n + 1)

    while pq:
        dist, node = heapq.heappop(pq)

        if ans[node] < dist:
            continue
        for next_node, weight in graph[node]:
            if node == x and next_node == y: # 만약 이번 for문에서 이 길을 막았으면
                continue

            new_dist = dist + weight
            if ans[next_node] < new_dist:
                continue
            ans[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))

    return ans[-1]

n, m = map(int, input().split())
graph = [[] for _ in range(m+1)] # 최단거리 구하기용 간선정보
block = []
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append([b, t])
    graph[b].append([a, t])


shortest = find_shortest(1) # 얘가 최단시간

ans = 0
for x, y in block:
    a = sol(1, x, y)
    ans = max(ans, a)
if ans == float('inf'):
    print(-1)
else:
    print(ans - shortest)

