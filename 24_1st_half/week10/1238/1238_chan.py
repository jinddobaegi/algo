import sys
sys.stdin = open('week10/1238/1238.txt')
input = sys.stdin.readline
import heapq

def dijkstra(start):
    q = []
    distance = [INF] * (nums+1) 
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for next, weight in graph[now]:
            new_dist = dist + weight
            if new_dist < distance[next]:
                distance[next] = new_dist
                heapq.heappush(q, (new_dist, next))
    return distance

INF = int(1e9)

nums, roads, goal = map(int, input().split())
graph = [[] for _ in range(nums+1)] # 1부터 시작하므로 nums+1
for _ in range(roads):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))

    
result = 0
for i in range(1, nums+1):
    go = dijkstra(i) #시작점 
    back = dijkstra(goal) #도착점
    result = max(result, go[goal] + back[i]) # 최대값을 찾는다

print(result)

